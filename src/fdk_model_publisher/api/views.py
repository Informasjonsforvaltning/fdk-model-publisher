from typing import Any

from aiohttp import hdrs, web

from fdk_model_publisher.service.fetcher import create_rdf_catalog, fetch_dataservices


class Catalog(web.View):
    @staticmethod
    async def get() -> Any:
        data_services = await fetch_dataservices()
        catalog = await create_rdf_catalog(data_services)
        return web.Response(
            text=str(catalog.to_rdf()), headers={hdrs.CONTENT_TYPE: "text/turtle"}
        )


class Ready(web.View):
    async def get(self) -> Any:
        """Ready route function."""
        if self.request.headers.get(hdrs.ACCEPT) != "application/json":
            return web.Response(text="OK")
        else:
            return web.Response(status=503)


class Ping(web.View):
    @staticmethod
    async def get() -> Any:
        """Ping route function."""
        return web.Response(text="OK")
