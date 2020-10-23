"""Integration test cases for the ready route."""
from flask import Flask
import pytest


@pytest.mark.integration
def test_ready(client: Flask) -> None:
    """Should return OK."""
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.data.decode() == "OK"


@pytest.mark.integration
def test_not_ready(client: Flask) -> None:
    """Should return Service Unavailable."""
    headers = {"Accept": "application/json"}
    response = client.get("/ready", headers=headers)

    assert response.status_code == 503
