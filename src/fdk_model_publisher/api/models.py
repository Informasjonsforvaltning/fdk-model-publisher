from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class RawModel:
    endpointDescription: Optional[str] = None
    schema: Optional[Dict] = None
