"""Module containing data models."""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class PartialInformationModel:
    """Partial information model model."""

    endpoint_description: Optional[str] = None
    schema: Optional[Dict] = None
