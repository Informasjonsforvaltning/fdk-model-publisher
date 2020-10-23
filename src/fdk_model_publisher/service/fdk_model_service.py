"""Service layer module for modelldcat-ap-no compliant information models from data service descriptions."""
from typing import Optional


def is_ready(accept_header: Optional[str]) -> bool:
    """Check if resource is available."""
    if accept_header == "application/json":
        return False
    else:
        return True
