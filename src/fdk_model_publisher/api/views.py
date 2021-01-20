"""Application view module.."""

import tracemalloc
from typing import Any

from aiohttp import hdrs, web

from fdk_model_publisher.service.fetcher import serialize_catalog


class Catalog(web.View):
    """Catalog view."""

    @staticmethod
    async def get() -> Any:
        """Get function for Catalog view."""
        catalog = await serialize_catalog()
        return web.Response(
            text=catalog,
            headers={hdrs.CONTENT_TYPE: "text/turtle"},
        )


class Ready(web.View):
    """Ready view."""

    @staticmethod
    async def get() -> Any:
        """Ready route function."""
        return web.Response(text="OK")


class Ping(web.View):
    """Ping view."""

    @staticmethod
    async def get() -> Any:
        """Ping route function."""
        return web.Response(text="OK")


class Mem(web.View):
    """Ping view."""

    @staticmethod
    async def get() -> Any:
        """Ping route function."""
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")
        top_10 = []
        for stat in top_stats[:10]:
            top_10.append(stat.__str__())
        return web.Response(text="\n".join(top_10))
