"""App factory and local dev entry point."""
import logging

from aiohttp import web

from fdk_model_publisher.api.routes import setup_routes
from fdk_model_publisher.service import fetcher, rabbit


async def create_app() -> web.Application:
    app = web.Application()
    app.on_startup.append(rabbit.listen)
    app.on_startup.append(fetcher.sync_rdf_catalog)

    app.on_cleanup.append(rabbit.close)
    app.on_cleanup.append(fetcher.sync_rdf_catalog_cleanup)
    setup_routes(app)
    return app


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    web.run_app(create_app())
