import gzip

from aiocache import caches

from fdk_model_publisher.config import Config

FDK_CATALOG_ID = "fdk_model_catalog"


caches.set_config(Config.cache_config())
cache = caches.get("default")


async def catalog_cache_exists() -> bool:
    return await cache.exists(FDK_CATALOG_ID)


async def delete_catalog_cache() -> None:
    await cache.delete(FDK_CATALOG_ID)


async def get_catalog_cache() -> str:
    return gzip.decompress(await cache.get(FDK_CATALOG_ID)).decode()


async def set_catalog_cache(serialized_catalog: str) -> None:
    await cache.set(FDK_CATALOG_ID, gzip.compress(serialized_catalog.encode()))
