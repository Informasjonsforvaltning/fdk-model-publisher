"""Application route module."""

from aiohttp import web

from fdk_model_publisher.api.views import Catalog, Mem, Ping, Ready


def setup_routes(app: web.Application) -> None:
    """Route set-up."""
    app.add_routes(
        [
            web.get("/ready", Ready),
            web.get("/ping", Ping),
            web.get("/mem", Mem),
            web.view("/catalog", Catalog),
        ]
    )
