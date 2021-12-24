import os

from .utils import *

__all__ = ('settings',)










class BaseConfig:
    """Base configuration."""
    DEBUG = False
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

    # redis
    REDIS_BROKER_CONFIG = get_redis_broker_configuration()
    REDIS_BACKEND_CONFIG = get_redis_backend_configuration()

    # mongo


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False


def load_config():
    return {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
    }.get(ENV, ProductionConfig)


settings = load_config()
