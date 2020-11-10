from typing import Any

from aiohttp import web

from service.fdk_model_service import is_ready


class Ready(web.View):
    async def get(self) -> Any:
        """Ready route function."""
        if is_ready(self.request.headers.get('Accept')):
            return web.Response(text='OK')
        else:
            return web.Response(status=500)


class Ping(web.View):
    """Class representing ping resource."""

    @staticmethod
    async def get() -> Any:
        """Ping route function."""
        return web.Response(text='OK')
