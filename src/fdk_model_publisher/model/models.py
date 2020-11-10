from dataclasses import dataclass
from typing import List, Optional


@dataclass
class InformationModelSource:
    identifier: Optional[str] = None
    endpointDescription: Optional[List[str]] = None
