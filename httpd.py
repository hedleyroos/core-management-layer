from management_layer import integration
from aiohttp import web
from management_layer.api.urls import add_routes
from management_layer.integration import user_data_api, authentication_api, access_control_api

async def hello(request):
    return web.Response(text="Hello, world")


async def on_shutdown(app):
    print("Waiting for clients to finish up...")
    await integration.access_control_api.api_client.rest_client.pool_manager.close()
    await integration.user_data_api.api_client.rest_client.pool_manager.close()
    await integration.authentication_api.api_client.rest_client.pool_manager.close()
    print("Done.")


if __name__ == "__main__":
    app = web.Application()
    app.on_shutdown.append(on_shutdown)
    add_routes(app)
    app.router.add_get('/', hello)
    web.run_app(app, port=8000)
