import os
from typing import Dict, Optional, Type, TypeVar

T = TypeVar("T", bound="Config")


class Config:
    _FDK_DATASERVICE_HARVESTER_URL: Optional[str] = None
    _FDK_MODEL_PUBLISHER_URI: Optional[str] = None

    _CACHE_PASSWORD: Optional[str] = os.getenv("CACHE_PASSWORD", None)

    _RABBITMQ: Dict[str, str] = {
        "name": os.getenv("RABBIT_USERNAME", "admin"),
        "pass": os.getenv("RABBIT_PASSWORD", "admin"),
        "host": os.getenv("RABBIT_HOST", "localhost"),
        "port": "5672",
        "exchange": "harvests",
    }

    @classmethod
    def rabbitmq_connection_string(cls: Type[T]) -> str:
        host = cls._RABBITMQ["host"]
        port = cls._RABBITMQ["port"]
        name = cls._RABBITMQ["name"]
        password = cls._RABBITMQ["pass"]
        return f"amqp://{name}:{password}@{host}:{port}"

    @classmethod
    def rabbitmq_exchange(cls: Type[T]) -> str:
        return cls._RABBITMQ["exchange"]

    @classmethod
    def fdk_dataservice_harvester_url(cls: Type[T]) -> Optional[str]:
        if cls._FDK_DATASERVICE_HARVESTER_URL is None:
            cls._FDK_DATASERVICE_HARVESTER_URL = os.getenv(
                "FDK_DATASERVICE_HARVESTER",
                "https://dataservices.staging.fellesdatakatalog.digdir.no",
            )
        return cls._FDK_DATASERVICE_HARVESTER_URL

    @classmethod
    def fdk_model_publisher_uri(cls: Type[T]) -> Optional[str]:
        if cls._FDK_MODEL_PUBLISHER_URI is None:
            cls._FDK_MODEL_PUBLISHER_URI = os.getenv(
                "FDK_MODEL_PUBLISHER_URI",
                "https://fdk-model-publisher.fellesdatakatalog.no",
            )
        return cls._FDK_MODEL_PUBLISHER_URI

    @classmethod
    def cache_config(cls: Type[T]) -> Dict:
        config = {
            "default": {
                "cache": "aiocache.RedisCache",
                "endpoint": "fdk-publishers-cache",
                "port": 6379,
                "serializer": {"class": "aiocache.serializers.PickleSerializer"},
                "plugins": [
                    {"class": "aiocache.plugins.HitMissRatioPlugin"},
                    {"class": "aiocache.plugins.TimingPlugin"},
                ],
            },
        }
        if cls._CACHE_PASSWORD:
            config["default"]["password"] = cls._CACHE_PASSWORD

        return config
