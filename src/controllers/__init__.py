from flask import Flask

from .usage import blueprints as usage_blueprint


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(usage_blueprint)
