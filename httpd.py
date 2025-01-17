# Import our customised logging module first in order for the settings to
# be applied to all the modules imported below.
import prometheus_client

from management_layer.logging import logging

import asyncio
import aioredis
from aiohttp import web, ClientSession
import aiojobs
from aiojobs.aiohttp import setup

import access_control
import authentication_service
import user_data_store
from management_layer import settings, views, integration
from management_layer.api.urls import add_routes
from management_layer.mappings import refresh_all
from management_layer.middleware import auth_middleware, sentry_middleware, metrics_middleware
from management_layer.settings import REDIS, MAPPING_REFRESH_SLEEP_SECONDS
from management_layer.metrics import add_prometheus_metrics_for_class

logger = logging.getLogger()
logger.setLevel(settings.LOG_LEVEL)


async def on_startup(application: web.Application):
    application["client_session"] = ClientSession()

    application["redis"] = await aioredis.create_redis_pool(REDIS, minsize=5, maxsize=10)

    logger.info("Setting up scheduled jobs...")

    # Create a closure that will be used to refresh data.
    # The closure contains the application, which is required for the API calls
    # which are used to refresh the data.
    async def refresh_mappings(sleep_secs: float):
        while True:
            await refresh_all(application)
            await asyncio.sleep(sleep_secs)

    scheduler = aiojobs.aiohttp.get_scheduler_from_app(app)
    await scheduler.spawn(refresh_mappings(MAPPING_REFRESH_SLEEP_SECONDS))


async def on_shutdown(app):
    logger.info("Waiting for client session to finish up...")
    await app["client_session"].close()
    logger.info("Waiting for redis to finish up...")
    app["redis"].close()
    await app["redis"].wait_closed()
    logger.info("Waiting for clients to finish up...")
    for backend in [
        "access_control_api",
        "operational_api",
        "authentication_service_api",
        "user_data_api"
    ]:
        await app[backend].api_client.rest_client.pool_manager.close()

    logger.info("Done.")


async def metrics(request):
    resp = web.Response(body=prometheus_client.generate_latest())
    resp.content_type = prometheus_client.CONTENT_TYPE_LATEST
    return resp


if __name__ == "__main__":
    # Add metric decorators to API functions
    add_prometheus_metrics_for_class(integration.Implementation)

    app = web.Application(middlewares=[
        metrics_middleware, sentry_middleware, auth_middleware
    ])

    logger.info("Using the following APIs:")
    user_data_store_configuration = user_data_store.configuration.Configuration()
    override_host = settings.USER_DATA_STORE_API
    if override_host:
        user_data_store_configuration.host = override_host
    app["user_data_api"] = user_data_store.api.UserDataApi(
        api_client=user_data_store.ApiClient(
            header_name="X-API-KEY",
            header_value=settings.USER_DATA_STORE_API_KEY,
            configuration=user_data_store_configuration
        )
    )

    access_control_configuration = access_control.configuration.Configuration()
    override_host = settings.ACCESS_CONTROL_API
    if override_host:
        access_control_configuration.host = override_host
    access_control_api_client = access_control.ApiClient(
        header_name="X-API-KEY",
        header_value=settings.ACCESS_CONTROL_API_KEY,
        configuration=access_control_configuration
    )
    app["access_control_api"] = access_control.api.AccessControlApi(
        api_client=access_control_api_client
    )

    # Operational API is a part of access control. It was split out by the
    # swagger generator due to its tag. Thus allowing it to use the same client
    # and config as access_control.
    app["operational_api"] = access_control.api.OperationalApi(
         api_client=access_control_api_client
    )

    authentication_service_configuration = authentication_service.configuration.Configuration()
    override_host = settings.AUTHENTICATION_SERVICE_API
    if override_host:
        authentication_service_configuration.host = override_host
    app["authentication_service_api"] = authentication_service.api.AuthenticationApi(
        api_client=authentication_service.ApiClient(
            header_name="X-API-KEY",
            header_value=settings.AUTHENTICATION_SERVICE_API_KEY,
            configuration=authentication_service_configuration
        )
    )

    logger.info("Access Control/Operational: {}".format(access_control_configuration.host))
    logger.info("Authentication Service: {}".format(authentication_service_configuration.host))
    logger.info("User Data Store: {}".format(user_data_store_configuration.host))
    logger.info("Redis: {}".format(REDIS))

    setup(app)  # Set up aiojobs scheduler
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    add_routes(app, with_ui=settings.WITH_UI)
    if settings.WITH_UI:
        # Override default spec view.
        app.router._resources = [
            resource for resource in app.router._resources
            if not hasattr(resource, "_path") or resource._path != "/the_specification"
        ]
        app.router.add_view(r"/the_specification", views.SwaggerSpec)

    # Add Prometheus metrics end-point
    app.router.add_get("/metrics", metrics)

    logger.info("Listening on port {}".format(settings.PORT))
    web.run_app(app, port=settings.PORT)
