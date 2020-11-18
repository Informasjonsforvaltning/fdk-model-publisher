from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class PartialInformationModel:
    endpointDescription: Optional[str] = None
    schema: Optional[Dict] = None
