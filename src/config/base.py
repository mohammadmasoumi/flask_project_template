import os

from .utils import get_env_var

BASEDIR = os.path.abspath(os.path.dirname(__name__))

PROJECT_NAME = 'app_server'
ENV = get_env_var("FLASK_ENV", "production")
FLASK_APP = get_env_var("FLASK_ENV", "app")

# logging
LOG_LEVEL = get_env_var("LOG_LEVEL", "DEBUG")

# mongo env
MONGO_DB = get_env_var('MONGO_DB', default='challenge', prefixed=True)
MONGO_HOST = get_env_var('MONGO_HOST', default='mongo', prefixed=True)
MONGO_PORT = int(get_env_var('MONGO_PORT', default=27017, prefixed=True))
MONGO_USERNAME = get_env_var('MONGO_USERNAME', default='challenge', prefixed=True)
MONGO_PASSWORD = get_env_var('MONGO_PASSWORD', default='challenge', prefixed=True)

# redis env
REDIS_HOST = get_env_var('REDIS_HOST', '')
REDIS_SENTINEL = get_env_var('REDIS_SENTINEL', '')
REDIS_PORT = get_env_var('REDIS_PORT', '')
REDIS_DB = get_env_var('REDIS_DB', '')
REDIS_PASSWORD = get_env_var('REDIS_PASSWORD', '')
REDIS_SENTINEL_MASTER = get_env_var('REDIS_SENTINEL_MASTER', '')

# celery config
CELERY_TIMEZONE = get_env_var("CELERY_TIMEZONE", "UTC")
