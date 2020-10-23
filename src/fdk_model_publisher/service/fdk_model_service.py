from typing import Optional


def is_ready(accept_header: Optional[str]) -> bool:
    if accept_header == "application/json":
        return False
    else:
        return True
