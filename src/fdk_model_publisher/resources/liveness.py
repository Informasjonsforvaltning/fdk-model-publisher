"""Resource module for ready."""
from typing import Any

from flask import abort, request, Response
from flask_restful import Resource

from fdk_model_publisher.service.fdk_model_service import is_ready


class Ready(Resource):
    """Class representing ready resource."""

    @staticmethod
    def get() -> Any:
        """Ready route function."""
        if is_ready(request.headers.get("Accept")):
            return Response("OK")
        else:
            abort(503)


class Ping(Resource):
    """Class representing ping resource."""

    @staticmethod
    def get() -> Response:
        """Ping route function."""
        return Response("OK")
