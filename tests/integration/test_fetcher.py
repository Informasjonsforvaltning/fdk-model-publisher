"""Integration test cases for the fetcher service module."""
from typing import Any

from async_timeout import timeout
from fdk_rdf_parser.fdk_rdf_parser import DataService
import pytest

from fdk_model_publisher.service.fetcher import parallel_fetch_and_map, TIMEOUT_SECONDS


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
    assert f"Timed out connecting to {endpoint}" in caplog.text
