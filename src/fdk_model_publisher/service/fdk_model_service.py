"""Service layer module for modelldcat-ap-no compliant information models from data service descriptions."""
import asyncio
from time import time
from typing import Optional, List, Dict, Tuple

import aiohttp
from aiohttp import ClientSession
from fdk_rdf_parser import fdk_rdf_parser as fdk, parse_data_services

from model import InformationModelSource

MAXIMUM_FILE_DESCRIPTORS = 10


def is_ready(accept_header: Optional[str]) -> bool:
    """Check if resource is available."""
    if accept_header == "application/json":
        return False
    else:
        return True


def create_information_model():
    pass


async def fetch(urls: List[str], session: ClientSession):
    # TODO: url here is a list of urls, do for loop it will still be async
    try:
        # TODO: temp urls[0], should be a for loop
        async with session.get(urls[0]) as response:
            response.raise_for_status()
            # do not use json() because rawgithubusercontent returns mimetype==
            success = await response.json(content_type='/')
            return success
    except aiohttp.ClientConnectionError as e:
        print(e)
        return None
    except aiohttp.ContentTypeError as e:
        # could not parse json
        print(e)
        return None
    except Exception as e:
        print(f'Dunno {e} / {response.url}')
        return None


async def bound_fetch(semaphore: asyncio.Semaphore, urls: List[str], session: ClientSession):
    # Getter function with semaphore.
    async with semaphore:
        return await fetch(urls, session)


async def run(information_model_sources: List[InformationModelSource]):
    tasks: List[asyncio.Future] = []

    semaphore = asyncio.Semaphore(MAXIMUM_FILE_DESCRIPTORS)  # maximum number of concurrent requests
    async with ClientSession(headers={'accept': 'application/json'}) as session:
        for source in information_model_sources:
            task = asyncio.ensure_future(bound_fetch(semaphore, source.endpointDescription, session))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        return await responses


def as_information_model_source(x: Tuple[str, fdk.DataService]):
    return InformationModelSource(identifier=x[0], endpointDescription=x[1].endpointDescription)


def has_endpoint_description(information_model_source: InformationModelSource):
    return information_model_source.endpointDescription is not None


# TODO: wrap parse_data_services in executor and await
async def create_rdf_catalog(data_services_rdf: str):
    data_services: Dict[str, fdk.DataService] = parse_data_services(data_services_rdf)
    populated = list(filter(has_endpoint_description, map(as_information_model_source, data_services.items())))

    # TODO: remove test limit
    # populated = populated[0:10]
    ### END ###

    start = time()
    resps = await run(populated)
    print(f'elapsed: {time() - start}')
    # print(resps)
