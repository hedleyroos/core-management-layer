from aiohttp import web
from management_layer.api.urls import add_routes

async def hello(request):
    return web.Response(text="Hello, world")

if __name__ == "__main__":
    app = web.Application()
    add_routes(app)
    app.router.add_get('/', hello)
    web.run_app(app, port=8000)
