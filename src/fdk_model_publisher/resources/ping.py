"""Resource module for ping."""
from flask import Response
from flask_restful import Resource


class Ping(Resource):
    """Class representing ping resource."""

    @staticmethod
    def get() -> Response:
        """Ping route function."""
        return Response("OK")
