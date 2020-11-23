"""Integration test cases for the ping route."""
import os
from typing import Any

import pytest
from aiohttp import ClientResponse, hdrs
from aiohttp.test_utils import TestClient
from aioresponses import aioresponses

FDK_DATASERVICE_HARVESTER_URL = os.getenv(
    "FDK_DATASERVICE_HARVESTER",
    "https://dataservices.staging.fellesdatakatalog.digdir.no",
)


@pytest.fixture
def mock_aio_response() -> Any:
    with aioresponses(passthrough=["http://127.0.0.1:"]) as m:
        m.add(url=f"{FDK_DATASERVICE_HARVESTER_URL}/catalogs", body="Hello, world")
        yield m


# @pytest.mark.integration
# async def test_catalog(cli: TestClient, mock_aio_response: Any) -> Any:
#     resp = await cli.get("/catalog")
#     assert resp.status == 200
#     text = await resp.text()
#     assert "Hello, world" in text


#  Server Health
@pytest.mark.integration
async def test_ping(cli: TestClient) -> Any:
    """Should return OK."""
    response: ClientResponse = await cli.get("/ping")

    assert response.status == 200
    text = await response.text()
    assert "OK" in text


@pytest.mark.integration
async def test_ready(cli: TestClient) -> Any:
    """Should return OK."""
    response: ClientResponse = await cli.get("/ready")
    assert response.status == 200
    text = await response.text()
    assert "OK" in text


@pytest.mark.integration
async def test_not_ready(cli: TestClient) -> Any:
    """Should return Service Unavailable."""
    headers = {hdrs.ACCEPT: "application/json"}
    response: ClientResponse = await cli.get("/ready", headers=headers)
    assert response.status == 503
