"""App factory and local dev entry point."""
import logging

from aiohttp import web

from fdk_model_publisher.api.routes import setup_routes


async def create_app() -> web.Application:
    logging.basicConfig(level=logging.INFO)
    app = web.Application()
    setup_routes(app)
    return app


if __name__ == "__main__":
    web.run_app(create_app())
