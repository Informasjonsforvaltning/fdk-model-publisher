"""Integration test cases for the ping route."""
import json
import os
from typing import Any

from aiohttp import ClientResponse
from aiohttp.test_utils import TestClient
from aioresponses import aioresponses
from fdk_rdf_parser.reference_data.utils import base_url
import pytest
from pytest_mock import MockFixture
from rdflib import Graph
from rdflib.compare import isomorphic

from .utils import _dump_diff, SkolemUtils
from ..mocks import (
    data_services_catalog_ttl_mock,
    skagerrak_sparebank_ttl_mock,
)

FDK_DATASERVICE_HARVESTER_URL = os.getenv(
    "FDK_DATASERVICE_HARVESTER",
    "https://dataservices.staging.fellesdatakatalog.digdir.no",
)

MOCK_URL = "https://mockurl.com"


@pytest.fixture
def mock_aio_response() -> Any:
    """Mock aio response."""
    with open("./tests/mocks/skagerrak_sparebank.json") as json_file:
        skagerrak_sparebank_json_mock = json.load(json_file)

    with aioresponses(passthrough=["http://127.0.0.1:"]) as m:
        m.add(
            url=f"{FDK_DATASERVICE_HARVESTER_URL}/catalogs?catalogrecords=true",
            body=data_services_catalog_ttl_mock,
        )
        m.add(
            url=f"{MOCK_URL}/Skagerrak_Sparebank_937891245_Accounts-API.json",
            payload=skagerrak_sparebank_json_mock,
        )
        yield m


@pytest.mark.integration
async def test_get_catalog(
    cli: TestClient, mock_get_skagerrak_from_cache: Any, mock_cache_exists: Any
) -> Any:
    """Get catalog test."""
    resp = await cli.get("/catalog")
    assert resp.status == 200
    text = await resp.text()

    expected = Graph().parse(data=skagerrak_sparebank_ttl_mock, format="turtle")
    actual = Graph().parse(data=text, format="turtle")
    assert actual.isomorphic(expected)


@pytest.mark.integration
async def test_set_catalog(
    cli: TestClient,
    mock_aio_response: Any,
    mock_set_cache: Any,
    mock_cache_does_not_exist: Any,
    mocker: MockFixture,
) -> Any:
    """Test catalog view."""
    skolemutils = SkolemUtils(base_url)

    mocker.patch(
        "skolemizer.Skolemizer.add_skolemization",
        side_effect=skolemutils.get_skolemization,
    )

    resp = await cli.get("/catalog")
    assert resp.status == 200
    text = await resp.text()

    expected = Graph().parse(data=skagerrak_sparebank_ttl_mock, format="turtle")
    actual = Graph().parse(data=text, format="turtle")

    _isomorphic = isomorphic(expected, actual)

    if not _isomorphic:
        _dump_diff(expected, actual)
        pass
    assert _isomorphic


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
