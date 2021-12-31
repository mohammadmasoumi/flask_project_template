from .app import config  # NOQA
from .celery import celery_config  # NOQA

__all__ = ('config', 'celery_config')

# configs
config = config
celery_config = celery_config
