"""Unit test cases for the model service module."""
import pytest

from fdk_model_publisher.service.fdk_model_service import is_ready


@pytest.mark.unit
def test_is_ready() -> None:
    """Should return True when ready."""
    _result = is_ready(None)

    assert _result is True


@pytest.mark.unit
def test_is_not_ready() -> None:
    """Should return False when not ready."""
    _result = is_ready("application/json")

    assert _result is False
