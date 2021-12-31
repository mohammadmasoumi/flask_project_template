from .base import *

__all__ = ('config',)


class Config:
    DEBUG = False
    FLASK_APP = FLASK_APP
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(16).hex())
    MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    CELERY_SEND_SENT_EVENT = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


# return active config
available_configs = dict(development=DevelopmentConfig, production=ProductionConfig)
config = available_configs.get(ENV, "production")
