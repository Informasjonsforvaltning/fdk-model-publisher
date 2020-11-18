import os
from typing import Any

from aiohttp import web, hdrs, ClientSession
from service.fetcher import is_ready


FDK_DATASERVICE_HARVESTER_BASE_URL = os.getenv(
    "FDK_DATASERVICE_HARVESTER",
    "https://dataservices.staging.fellesdatakatalog.digdir.no",
)


class Catalog(web.View):
    @staticmethod
    async def get() -> Any:
        async with ClientSession(headers={"Accept": "text/turtle"}) as session:
            async with session.get(
                url=f"{FDK_DATASERVICE_HARVESTER_BASE_URL}/catalogs"
            ) as r:
                r.raise_for_status()
                data_services = await r.text()
                return web.json_response(data_services, status=200)
                # catalog = await create_rdf_catalog(data_services)
                # return web.json_response(catalog.to_rdf())


class Ready(web.View):
    async def get(self) -> Any:
        """Ready route function."""
        if self.request.headers.get(hdrs.ACCEPT) == "application/json":
            return web.Response(text="OK")
        else:
            return web.Response(status=503)


class Ping(web.View):
    """Class representing ping resource."""

    @staticmethod
    async def get() -> Any:
        """Ping route function."""
        return web.Response(text="OK")
