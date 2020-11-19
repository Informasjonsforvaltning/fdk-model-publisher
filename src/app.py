"""App factory and local dev entry point."""
import logging

from aiohttp import web
from api.routes import setup_routes


async def create_app() -> web.Application:
    app = web.Application()
    setup_routes(app)
    return app


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    web.run_app(create_app())
