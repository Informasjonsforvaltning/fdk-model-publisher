"""Service layer module for modelldcat-ap-no compliant information models from data service descriptions."""
import asyncio
import logging
import os
from typing import Any, Dict, List, Tuple

import aiohttp
import yaml
from aiohttp import ClientSession, hdrs
from datacatalogtordf import Catalog

from fdk_model_publisher.api.models import PartialInformationModel

from fdk_rdf_parser import parse_data_services
from fdk_rdf_parser.fdk_rdf_parser import DataService

from .mapper import create_catalog, map_model_from_dict

FDK_DATASERVICE_HARVESTER_BASE_URL = os.getenv(
    "FDK_DATASERVICE_HARVESTER",
    "https://dataservices.staging.fellesdatakatalog.digdir.no",
)

MAXIMUM_FILE_DESCRIPTORS = 50


async def fetch_dataservice_catalog() -> str:
    async with ClientSession(headers={hdrs.ACCEPT: "text/turtle"}) as session:
        async with session.get(
            url=f"{FDK_DATASERVICE_HARVESTER_BASE_URL}/catalogs"
        ) as r:
            r.raise_for_status()
            return await r.text()


async def fetch(session: ClientSession, urls: List[str]) -> PartialInformationModel:
    # urls[0] because in practice there should only be 1 element
    model = PartialInformationModel(endpoint_description=urls[0])
    try:
        async with session.get(urls[0]) as response:
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
    return model


async def fetch_with_sem(
    semaphore: asyncio.Semaphore, session: ClientSession, data_service: DataService
) -> Tuple[DataService, PartialInformationModel]:
    # fetch function with semaphore.
    async with semaphore:
        partial_model = await fetch(session, data_service.endpointDescription)
        return data_service, partial_model


async def parallel_fetch_and_map(data_services: List[DataService]) -> Any:
    tasks: List[asyncio.Future] = []

    # maximum number of concurrent requests
    semaphore = asyncio.Semaphore(MAXIMUM_FILE_DESCRIPTORS)

    async with ClientSession(headers={hdrs.ACCEPT: "application/json"}) as session:
        for data_service in data_services:
            task = asyncio.create_task(
                fetch_with_sem(semaphore, session, data_service),
            )
            tasks.append(task)

        partial_models = await asyncio.gather(*tasks)

        return [
            map_model_from_dict(partial_model, data_service)
            for (data_service, partial_model) in partial_models
            if partial_model.schema and "components" in partial_model.schema
        ]


async def create_rdf_catalog(data_services_rdf: str) -> Catalog:
    data_services: Dict[str, DataService] = parse_data_services(data_services_rdf)

    # filter only those that have endpointDescription with at least 1 element in it
    info_model_sources = [
        data_service
        for key, data_service in data_services.items()
        if data_service.endpointDescription
    ]

    information_models = await parallel_fetch_and_map(info_model_sources)

    return create_catalog(information_models)
