from .base import *

__all__ = ('celery_config',)


class BaseCeleryConfig:
    enable_utc = True
    timezone = CELERY_TIMEZONE
    result_expires = 3600


class DevelopmentCeleryConfig(BaseCeleryConfig):
    # broker url
    broker_url = REDIS_SENTINEL
    broker_transport_options = {
        'master_name': REDIS_SENTINEL_MASTER,
        'sentinel_kwargs': {'password': REDIS_PASSWORD}
    }

    # result backend
    result_backend = REDIS_SENTINEL
    result_backend_transport_options = {
        'master_name': REDIS_SENTINEL_MASTER,
        'sentinel_kwargs': {'password': REDIS_PASSWORD}
    }


class ProductionCeleryConfig(BaseCeleryConfig):
    # broker url
    broker_url = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

    # result backend
    result_backend = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",


# return active config
available_configs = dict(development=DevelopmentCeleryConfig, production=ProductionCeleryConfig)
celery_config = available_configs.get(ENV, "production")
