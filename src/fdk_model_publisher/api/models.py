from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class PartialInformationModel:
    endpoint_description: Optional[str] = None
    schema: Optional[Dict] = None
