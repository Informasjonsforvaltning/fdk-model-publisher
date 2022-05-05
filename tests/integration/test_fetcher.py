"""Integration test cases for the fetcher service module."""
from typing import Any

from aiohttp import hdrs
from aioresponses import aioresponses
from async_timeout import timeout
from fdk_rdf_parser.fdk_rdf_parser import DataService
import pytest

from fdk_model_publisher.service.fetcher import parallel_fetch_and_map, TIMEOUT_SECONDS


MOCK_URL = "https://mockurl.com"


@pytest.mark.integration
async def test_timeout(caplog: Any) -> None:
    """Test timeout."""
    endpoint = "http://10.255.255.255"  # non-routable IP
    ds = DataService(
        title={"nb": "timeout endpoint"},
        endpointDescription={endpoint},
        uri=endpoint,
    )

    with timeout(TIMEOUT_SECONDS + 1):
        result = await parallel_fetch_and_map([ds])

    assert result == []
    assert "ERROR" in caplog.text
    assert f"Timed out connecting to {endpoint}" in caplog.text


@pytest.mark.integration
async def test_non_json_200(caplog: Any) -> None:
    """Test 200 response that is not json parsable."""
    endpoint = f"{MOCK_URL}/non-json"

    with aioresponses(passthrough=["http://127.0.0.1:"]) as m:
        m.add(
            url=endpoint,
            body="<!DOCTYPE html><html></html>",
            headers={hdrs.CONTENT_TYPE: "text/html; charset=utf-8"},
        )

        ds = DataService(
            title={"nb": "timeout endpoint"},
            endpointDescription={endpoint},
            uri=endpoint,
        )

        with timeout(1):
            result = await parallel_fetch_and_map([ds])

        assert result == []
        assert "WARNING" in caplog.text
        assert f"Wrong content type for {endpoint}" in caplog.text
