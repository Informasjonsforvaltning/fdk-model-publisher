"""Conftest module."""
from asyncio import AbstractEventLoop
from os import environ as env
from typing import Any
from unittest.mock import AsyncMock

import pytest
from pytest_mock import MockFixture

from src.fdk_model_publisher.app import create_app  # type: ignore

from dotenv import load_dotenv

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
