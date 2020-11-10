"""Service layer module for modelldcat-ap-no compliant information models from data service descriptions."""
import asyncio
from time import time
from typing import Optional, List, Dict, Tuple


import yaml
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


async def fetch(session: ClientSession, urls: List[str]):
    try:
        # TODO: temp urls[0], should be a for loop
        async with session.get(urls[0]) as response:
            response.raise_for_status()

            if response.url.raw_path.endswith('.yaml'):
                # TODO: wrap in executor
                return yaml.safe_load(await response.read())
            # content_type='/' will ensure all mimetypes with a slash in them
            # Bad design from aiohttp
            return await response.json(content_type='/', encoding='utf-8-sig')

    except (aiohttp.ClientConnectionError, aiohttp.ContentTypeError) as e:
        # could not parse json
        print(e)
        return None
    except Exception as e:
        print(f'Dunno {e} / {response.url}')
        return None


async def bound_fetch(semaphore: asyncio.Semaphore, session: ClientSession, urls: List[str]):
    # Getter function with semaphore.
    async with semaphore:
        return await fetch(session, urls)


async def run(information_model_sources: List[InformationModelSource]):
    tasks: List[asyncio.Future] = []

    semaphore = asyncio.Semaphore(MAXIMUM_FILE_DESCRIPTORS)  # maximum number of concurrent requests
    async with ClientSession(headers={'accept': 'application/json'}) as session:
        for source in information_model_sources:
            task = asyncio.ensure_future(
                bound_fetch(semaphore, session, urls=source.endpointDescription)
            )
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
    populated = list(
        filter(has_endpoint_description,
               map(as_information_model_source, data_services.items())))

    start = time()
    resps = await run(populated)
    print(f'elapsed: {time() - start}')
    print('done')
    # print(resps)
