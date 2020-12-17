from typing import Any

from aiohttp import hdrs, web

from fdk_model_publisher.service.fetcher import serialize_catalog


class Catalog(web.View):
    @staticmethod
    async def get() -> Any:
        catalog = await serialize_catalog()
        return web.Response(
            text=catalog,
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
