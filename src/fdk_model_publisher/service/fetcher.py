"""Service layer module for modelldcat-ap-no compliant information models from data service descriptions."""
import asyncio
import logging
from typing import Any, Dict, List, Optional

import aiohttp
import yaml
from aiohttp import ClientSession, hdrs
from api.models import PartialInformationModel
from datacatalogtordf import Catalog
from fdk_rdf_parser import parse_data_services
from fdk_rdf_parser.fdk_rdf_parser import DataService
from modelldcatnotordf.agent import Agent
from modelldcatnotordf.informationmodel import InformationModel

from .mapper import map_model_from_dict

MAXIMUM_FILE_DESCRIPTORS = 10


async def fetch(session: ClientSession, urls: List[str]) -> PartialInformationModel:
    models = [PartialInformationModel(endpoint_description=url) for url in urls]

    for model in models:
        try:
            async with session.get(model.endpoint_description) as response:
                response.raise_for_status()

                if response.url.raw_path.endswith(".yaml"):
                    model.schema = yaml.safe_load(await response.read())
                else:
                    model.schema = await response.json(
                        content_type=response.headers.get(hdrs.CONTENT_TYPE),
                        encoding="utf-8-sig",
                    )
        except (aiohttp.ClientConnectionError, aiohttp.ContentTypeError) as e:
            logging.error(e)
        except Exception as e:
            logging.error(f"unknown error:{e}")
    # TODO: temp [0], should only be 1 I think and also remove the upper for loop
    return models[0]


async def fetch_and_map(
    semaphore: asyncio.Semaphore, session: ClientSession, data_service: DataService
) -> Optional[InformationModel]:
    # fetch function with semaphore.
    async with semaphore:
        raw_model = await fetch(session, data_service.endpointDescription)
        if raw_model.schema and "components" in raw_model.schema:
            return map_model_from_dict(raw_model, data_service)
            # return raw_model
        return None


async def parallel_fetch_and_map(data_services: List[DataService]) -> Any:
    tasks: List[asyncio.Future] = []

    # maximum number of concurrent requests
    semaphore = asyncio.Semaphore(MAXIMUM_FILE_DESCRIPTORS)

    async with ClientSession(headers={hdrs.ACCEPT: "application/json"}) as session:
        for data_service in data_services:
            task = asyncio.create_task(
                fetch_and_map(semaphore, session, data_service),
            )
            tasks.append(task)

        return await asyncio.gather(*tasks)


async def create_rdf_catalog(data_services_rdf: str) -> Catalog:
    data_services: Dict[str, DataService] = parse_data_services(data_services_rdf)

    # filter only those that have endpointDescription with at least 1 element in it
    info_model_sources = [
        data_service
        for key, data_service in data_services.items()
        if data_service.endpointDescription
    ]

    # process all models that are not null into catalog
    catalog = Catalog()

    catalog.title = {"en": "A dataset catalog"}  # TODO: where to get it from ?
    catalog.models = [
        model for model in await parallel_fetch_and_map(info_model_sources) if model
    ]
    catalog.identifier = "http://example.com/catalogs/1"  # TODO: where to get it from ?

    for i in range(len(catalog.models)):
        agent = Agent()
        agent.name = {"en": "James Bond", "nb": "Djeims Bånd"}
        agent.identifier = f"http://example.com/catalogs/{i}"
        catalog.models[i].publisher = agent  # TODO: where to get it from ?

    # rdf = catalog.to_rdf()

    return catalog
