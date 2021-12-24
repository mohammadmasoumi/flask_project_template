from celery import Celery
from flask_pymongo import PyMongo

from config import celery_config

__all__ = (
    'celery',
    'register_extensions'
)

# extensions
celery = Celery()
pymongo = PyMongo()


def register_extensions(app, worker=False):
    # load celery config
    celery.config_from_object(celery_config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    # pymongo
    pymongo.init_app(app)

    if not worker:
        pass
