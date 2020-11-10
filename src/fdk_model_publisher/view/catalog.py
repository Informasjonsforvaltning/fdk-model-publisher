import os
from typing import Any

from aiohttp import web, ClientSession

from service.fdk_model_service import create_rdf_catalog

FDK_DATASERVICE_HARVESTER_BASE_URL = os.getenv('FDK_DATASERVICE_HARVESTER',
                                               'https://dataservices.staging.fellesdatakatalog.digdir.no')


class Catalog(web.View):

    @staticmethod
    async def get() -> Any:
        async with ClientSession(headers={'Accept': 'text/turtle'}) as session:
            async with session.get(url=f'{FDK_DATASERVICE_HARVESTER_BASE_URL}/catalogs') as r:
                r.raise_for_status()
                data_services = await r.text()
                return web.json_response(await create_rdf_catalog(data_services))
