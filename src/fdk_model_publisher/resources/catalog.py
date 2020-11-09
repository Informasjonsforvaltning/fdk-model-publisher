import os
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR
from typing import Any

import requests
from flask_restful import Resource, abort

from ..service.fdk_model_service import create_rdf_catalog

FDK_DATASERVICE_HARVESTER_BASE_URL = os.getenv('FDK_DATASERVICE_HARVESTER',
                                               'https://dataservices.staging.fellesdatakatalog.digdir.no')


class Catalog(Resource):

    def get(self, ) -> Any:
        try:
            response = requests.get(url=f'{FDK_DATASERVICE_HARVESTER_BASE_URL}/catalogs', headers={'Accept': 'text/turtle'}, timeout=10)
            response.raise_for_status()

            create_rdf_catalog(response.text)
        except:
            abort(INTERNAL_SERVER_ERROR)
