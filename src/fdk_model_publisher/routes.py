from aiohttp import web

from view import Ping, Ready, Catalog


def setup_routes(app: web.Application):
    app.add_routes([web.get('/ready', Ready),
                    web.get('/ping', Ping),
                    web.get('/catalog', Catalog)])
