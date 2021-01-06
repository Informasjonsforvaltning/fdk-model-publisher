"""Conftest module."""
from asyncio import AbstractEventLoop
from os import environ as env
from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest
from pytest_mock import MockFixture

from src.fdk_model_publisher.app import create_app  # type: ignore

from dotenv import load_dotenv

from .mocks import skagerrak_sparebank_ttl_mock

load_dotenv()
HOST_PORT = int(env.get("HOST_PORT", "8080"))


@pytest.mark.integration
@pytest.fixture(scope="function")
async def cli(mocker: MockFixture, loop: AbstractEventLoop, aiohttp_client: Any) -> Any:

    do_nothing_mock = AsyncMock()
    mocker.patch(
        "fdk_model_publisher.service.rabbit.listen", side_effect=do_nothing_mock
    )
    mocker.patch(
        "fdk_model_publisher.service.rabbit.close", side_effect=do_nothing_mock
    )
    mocker.patch(
        "fdk_model_publisher.service.fetcher.sync_rdf_catalog",
        side_effect=do_nothing_mock,
    )
    mocker.patch(
        "fdk_model_publisher.service.fetcher.sync_rdf_catalog_cleanup",
        side_effect=do_nothing_mock,
    )
    return await aiohttp_client(await create_app())


@pytest.fixture
def mock_get_skagerrak_from_cache(mocker: MockFixture) -> Mock:
    mock = mocker.patch("fdk_model_publisher.service.fetcher.get_catalog_cache")
    mock.return_value = skagerrak_sparebank_ttl_mock
    return mock


@pytest.fixture
def mock_set_cache(mocker: MockFixture) -> Mock:
    mock = mocker.patch("fdk_model_publisher.service.fetcher.set_catalog_cache")
    return mock


@pytest.fixture
def mock_cache_exists(mocker: MockFixture) -> Mock:
    mock = mocker.patch("fdk_model_publisher.service.fetcher.catalog_cache_exists")
    mock.return_value = True
    return mock


@pytest.fixture
def mock_cache_does_not_exist(mocker: MockFixture) -> Mock:
    mock = mocker.patch("fdk_model_publisher.service.fetcher.catalog_cache_exists")
    mock.return_value = False
    return mock
