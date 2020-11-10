from aiohttp import web

from routes import setup_routes


def create_app():
    app = web.Application()
    setup_routes(app)
    return app


if __name__ == "__main__":
    web_app = create_app()
    web.run_app(web_app)
