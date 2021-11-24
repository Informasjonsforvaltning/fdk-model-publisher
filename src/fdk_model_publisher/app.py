"""App factory and local dev entry point."""
import logging

from aiohttp import web

from fdk_model_publisher.api.routes import setup_routes
from fdk_model_publisher.service import fetcher, rabbit


async def create_app() -> web.Application:
    """App creation and route set-up."""
    app = web.Application()
    app.on_startup.append(rabbit.listen)
    app.on_startup.append(fetcher.sync_rdf_catalog)

    app.on_cleanup.append(rabbit.close)
    app.on_cleanup.append(fetcher.sync_rdf_catalog_cleanup)
    setup_routes(app)

    # logging configurataion:
    logging.basicConfig(
        format="%(asctime)s,%(msecs)d %(levelname)s - %(module)s:%(lineno)d: %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    logging.getLogger("chardet.charsetprober").setLevel(logging.INFO)

    return app


if __name__ == "__main__":
    web.run_app(create_app())
