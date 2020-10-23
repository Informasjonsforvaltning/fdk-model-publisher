"""Integration test cases for the ping route."""
from flask import Flask
import pytest


@pytest.mark.integration
def test_ping(client: Flask) -> None:
    """Should return OK."""
    response = client.get("/ping")

    assert response.status_code == 200
    assert response.data.decode() == "OK"
