"""Conftest module."""
from asyncio import AbstractEventLoop
from os import environ as env
from typing import Any

import pytest

from src.fdk_model_publisher.app import create_app  # type: ignore

from dotenv import load_dotenv

load_dotenv()
HOST_PORT = int(env.get("HOST_PORT", "8080"))


@pytest.mark.integration
@pytest.fixture(scope="function")
def cli(loop: AbstractEventLoop, aiohttp_client: Any) -> Any:
    return loop.run_until_complete(
        aiohttp_client(loop.run_until_complete(create_app()))
    )
