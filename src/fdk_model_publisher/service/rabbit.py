import asyncio
import functools
import logging

from typing import Coroutine, Optional

from aiohttp import web
from aio_pika import connect, Connection, ExchangeType, IncomingMessage

from fdk_model_publisher.config import Config
from fdk_model_publisher.service.fetcher import serialize_catalog


class AsyncDebounce:
    def __init__(self, timeout: int = 10) -> None:
        self._timeout: int = timeout
        self._timer_handle: Optional[asyncio.TimerHandle] = None

    def _scheduled(self) -> bool:
        return self._timer_handle is not None

    async def debounce(self, async_callback: Coroutine) -> None:
        # reset debounce if already scheduled
        if self._scheduled():
            self.cancel()

        self._timer_handle = asyncio.get_event_loop().call_later(
            delay=self._timeout,
            callback=functools.partial(asyncio.ensure_future, async_callback),
        )

    def cancel(self) -> None:
        if self._timer_handle:
            self._timer_handle.cancel()


limiter = AsyncDebounce(timeout=5)


async def on_message(message: IncomingMessage) -> None:
    async with message.process():
        logging.info(f"[x]{message.routing_key}")
        await limiter.debounce(async_callback=serialize_catalog(invalidate_cache=True))


async def close(app: web.Application) -> None:
    app["rabbit"]["listener"].cancel()
    await app["rabbit"]["listener"]
    await app["rabbit"]["connection"].close()


async def listen(app: web.Application) -> None:
    # Perform connection
    connection: Connection = await connect(
        Config.rabbitmq_connection_string(), loop=asyncio.get_event_loop()
    )

    # Creating a channel
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)

    # Declare an exchange
    topic_harvests_exchange = await channel.declare_exchange(
        "harvests", ExchangeType.TOPIC
    )

    # Declaring anonymous queue
    queue = await channel.declare_queue(durable=False, exclusive=True, auto_delete=True)

    await queue.bind(
        topic_harvests_exchange, routing_key="dataservice.*.HarvestTrigger"
    )

    # Start listening
    app["rabbit"] = {
        "connection": connection,
        "listener": asyncio.create_task(queue.consume(on_message)),
    }
