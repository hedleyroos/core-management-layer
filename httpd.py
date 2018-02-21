import os
from aiohttp import web

import access_control
import authentication_service
import user_data_store
from management_layer.api.urls import add_routes


async def on_shutdown(app):
    print("Waiting for clients to finish up...")
    for backend in ["access_control_api", "authentication_service_api", "user_data_api"]:
        await app[backend].api_client.rest_client.pool_manager.close()

    print("Done.")


if __name__ == "__main__":
    app = web.Application()
    print("Using the following APIs:")
    user_data_store_configuration = user_data_store.configuration.Configuration()
    override_host = os.getenv("USER_DATA_STORE_API")
    if override_host:
        user_data_store_configuration.host = override_host
    app["user_data_api"] = user_data_store.api.UserDataApi(
        api_client=user_data_store.ApiClient(
            configuration=user_data_store_configuration
        )
    )

    access_control_configuration = access_control.configuration.Configuration()
    override_host = os.getenv("ACCESS_CONTROL_API")
    if override_host:
        access_control_configuration.host = override_host
    app["access_control_api"] = access_control.api.AccessControlApi(
        api_client=access_control.ApiClient(
            configuration=access_control_configuration
        )
    )

    authentication_service_configuration = authentication_service.configuration.Configuration()
    override_host = os.getenv("AUTHENTICATION_SERVICE_API")
    if override_host:
        authentication_service_configuration.host = override_host
    app["authentication_service_api"] = authentication_service.api.AuthenticationApi(
        api_client=authentication_service.ApiClient(
            configuration=authentication_service_configuration
        )
    )

    print("Access Control: {}".format(access_control_configuration.host))
    print("Authentication Service: {}".format(authentication_service_configuration.host))
    print("User Data Store: {}".format(user_data_store_configuration.host))
    app.on_shutdown.append(on_shutdown)
    add_routes(app, with_ui=True)
    web.run_app(app, port=os.getenv("PORT", 8000))
