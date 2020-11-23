from aiohttp import web

from fdk_model_publisher.api.views import Catalog, Ping, Ready


def setup_routes(app: web.Application) -> None:
    app.add_routes(
        [
            web.get("/ready", Ready),
            web.get("/ping", Ping),
            web.view("/catalog", Catalog),
        ]
    )
