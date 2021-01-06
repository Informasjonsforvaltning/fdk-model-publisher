from typing import Any

from aiohttp import hdrs, web

from fdk_model_publisher.service.fetcher import (
    create_rdf_catalog,
    fetch_dataservice_catalog,
)


class Catalog(web.View):
    @staticmethod
    async def get() -> Any:
        data_services = await fetch_dataservice_catalog()
        catalog = await create_rdf_catalog(data_services)
        return web.Response(
            # TODO: report to_rdf typing bug, says: str, actual: bytes
            text=catalog.to_rdf(encoding="utf-8").decode("utf-8"),
            headers={hdrs.CONTENT_TYPE: "text/turtle"},
        )


class Ready(web.View):
    async def get(self) -> Any:
        """Ready route function."""
        return web.Response(text="OK")


class Ping(web.View):
    @staticmethod
    async def get() -> Any:
        """Ping route function."""
        return web.Response(text="OK")
