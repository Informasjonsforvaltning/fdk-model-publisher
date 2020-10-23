from typing import Any

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from .resources.ping import Ping
from .resources.ready import Ready

__version__ = "0.1.0"


def create_app(test_config: Any = None) -> Flask:
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Get environment
    load_dotenv()

    api = Api(app)

    # healthcheck routes
    api.add_resource(Ping, "/ping")
    api.add_resource(Ready, "/ready")

    return app
