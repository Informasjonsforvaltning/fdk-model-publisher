"""Utils module."""
import asyncio
from asyncio import AbstractEventLoop
from functools import partial, wraps
from typing import Any, Callable, Coroutine, Dict, Optional, Tuple


def async_wrap(func: Callable) -> Callable:
    """Async wrap method."""

    @wraps(func)
    async def run(
        *args: Tuple[Any, ...],
        loop: Optional[AbstractEventLoop] = None,
        executor: Any = None,
        **kwargs: Dict[str, Any]
    ) -> Coroutine:
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run
