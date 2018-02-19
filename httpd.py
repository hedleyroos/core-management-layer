import management_layer.configuration
from aiohttp import web
from management_layer.api.urls import add_routes


async def hello(request):
    return web.Response(text="Hello, world")


async def on_shutdown(app):
    print("Waiting for clients to finish up...")
    await management_layer.configuration.access_control_api.api_client.rest_client.pool_manager.close()
    await management_layer.configuration.user_data_api.api_client.rest_client.pool_manager.close()
    await management_layer.configuration.authentication_api.api_client.rest_client.pool_manager.close()
    print("Done.")


if __name__ == "__main__":
    app = web.Application()
    app.on_shutdown.append(on_shutdown)
    add_routes(app)
    app.router.add_get('/', hello)
    web.run_app(app, port=8000)
