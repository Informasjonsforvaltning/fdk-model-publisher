from aiohttp import web

from api.views import Catalog, Ping, Ready


def setup_routes(app: web.Application) -> None:
    app.add_routes(
        [web.get("/ready", Ready), web.get("/ping", Ping), web.get("/catalog", Catalog)]
    )
