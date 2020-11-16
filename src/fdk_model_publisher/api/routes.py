from aiohttp import web

from api.views import Ping, Ready, Catalog


def setup_routes(app: web.Application):
    app.add_routes([web.get('/ready', Ready),
                    web.get('/ping', Ping),
                    web.get('/catalog', Catalog)])
