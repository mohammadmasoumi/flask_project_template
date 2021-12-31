import logging
import sys

from flask import Flask

from src.app.config import config
# from src.controllers import register_blueprints
from src.app.factory.extensions import register_extensions

__all__ = (
    'create_app',
    'create_worker_app'
)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    # log level
    logging.basicConfig(level=logging.getLevelName(app.config['LOG_LEVEL']))
    logging.StreamHandler(sys.stdout)

    # register
    register_extensions(app)
    # register_blueprints(app)

    return app


def create_worker_app():
    """Minimal App without routes for celery worker."""
    app = Flask(__name__)
    app.config.from_object(config)

    # log level
    logging.basicConfig(level=logging.getLevelName(app.config['LOG_LEVEL']))
    logging.StreamHandler(sys.stdout)

    register_extensions(app, worker=True)

    return app
