from aiohttp import web
from management_layer.api.urls import add_routes
from management_layer import configuration


async def hello(request):
    return web.Response(text="Hello, world")


async def on_shutdown(app):
    print("Waiting for clients to finish up...")
    await configuration.access_control_api.api_client.rest_client.pool_manager.close()
    await configuration.user_data_api.api_client.rest_client.pool_manager.close()
    await configuration.authentication_api.api_client.rest_client.pool_manager.close()
    print("Done.")


if __name__ == "__main__":
    print("Using the following APIs:")
    print("Access Control: {}".format(configuration.access_control_configuration.host))
    print("Authentication Service: {}".format(configuration.authentication_configuration.host))
    print("User Data Store: {}".format(configuration.user_data_store_configuration.host))
    app = web.Application()
    app.on_shutdown.append(on_shutdown)
    add_routes(app)
    app.router.add_get('/', hello)
    web.run_app(app, port=8000)
