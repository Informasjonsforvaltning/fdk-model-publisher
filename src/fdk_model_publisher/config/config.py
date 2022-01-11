"""Configure fdk-model-publisher."""
import os
from typing import Dict, Optional, Type, TypeVar

T = TypeVar("T", bound="Config")


class Config:
    """Configuration class."""

    _FDK_REASONING_SERVICE_HOST: str = ""
    _FDK_MODEL_PUBLISHER_URI: str = ""
    _FDK_PUBLISHERS_BASE_URI: str = ""

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
        """Rabbit M.Q. connection string."""
        host = cls._RABBITMQ["host"]
        port = cls._RABBITMQ["port"]
        name = cls._RABBITMQ["name"]
        password = cls._RABBITMQ["pass"]
        return f"amqp://{name}:{password}@{host}:{port}"

    @classmethod
    def rabbitmq_exchange(cls: Type[T]) -> str:
        """Rabbit M.Q. exchange."""
        return cls._RABBITMQ["exchange"]

    @classmethod
    def fdk_reasoning_service_url(cls: Type[T]) -> str:
        """Reasoning service URL."""
        if cls._FDK_REASONING_SERVICE_HOST == "":
            cls._FDK_REASONING_SERVICE_HOST = os.getenv(
                "FDK_REASONING_SERVICE_HOST",
                "https://staging.fellesdatakatalog.digdir.no/reasoning",
            )
        return cls._FDK_REASONING_SERVICE_HOST

    @classmethod
    def fdk_publishers_base_uri(cls: Type[T]) -> str:
        """Model publisher URI."""
        if cls._FDK_PUBLISHERS_BASE_URI == "":
            cls._FDK_PUBLISHERS_BASE_URI = os.getenv(
                "FDK_PUBLISHERS_BASE_URI",
                "https://publishers.staging.fellesdatakatalog.digdir.no",
            )
        return cls._FDK_PUBLISHERS_BASE_URI

    @classmethod
    def fdk_model_publisher_uri(cls: Type[T]) -> str:
        """Model publisher URI."""
        if cls._FDK_MODEL_PUBLISHER_URI == "":
            cls._FDK_MODEL_PUBLISHER_URI = os.getenv(
                "FDK_MODEL_PUBLISHER_URI",
                "https://fdk-model-publisher.fellesdatakatalog.no",
            )
        return cls._FDK_MODEL_PUBLISHER_URI

    @classmethod
    def cache_config(cls: Type[T]) -> Dict:
        """Configure cache."""
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
