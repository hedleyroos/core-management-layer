import logging
from aiohttp import web

import access_control
import authentication_service
import user_data_store
from management_layer import settings, views
from management_layer.api.urls import add_routes
from management_layer.middleware import auth_middleware

logging.basicConfig(level=settings.LOG_LEVEL)


async def on_shutdown(app):
    print("Waiting for clients to finish up...")
    for backend in ["access_control_api", "authentication_service_api", "user_data_api"]:
        await app[backend].api_client.rest_client.pool_manager.close()

    print("Done.")


if __name__ == "__main__":
    if settings.INSECURE:
        print("*" * 29)
        print("* Running in insecure mode! *")
        print("*" * 29)

    app = web.Application(middlewares=[auth_middleware])
    print("Using the following APIs:")
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
    app["access_control_api"] = access_control.api.AccessControlApi(
        api_client=access_control.ApiClient(
            header_name="X-API-KEY",
            header_value=settings.ACCESS_CONTROL_API_KEY,
            configuration=access_control_configuration
        )
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

    print("Access Control: {}".format(access_control_configuration.host))
    print("Authentication Service: {}".format(authentication_service_configuration.host))
    print("User Data Store: {}".format(user_data_store_configuration.host))

    app.on_shutdown.append(on_shutdown)
    add_routes(app, with_ui=settings.WITH_UI)
    if settings.WITH_UI:
        # Override default spec view.
        app.router._resources = [
            resource for resource in app.router._resources
            if not hasattr(resource, "_path") or resource._path != "/the_specification"
        ]
        app.router.add_view(r"/the_specification", views.SwaggerSpec)

    print("Listening on port {}".format(settings.PORT))
    web.run_app(app, port=settings.PORT)
