import os

_PREFIX = 'APP_'


def get_env_var(name, default=None, prefixed=False):
    """ Returns the value of the environment variable with th given name
    :param name: name of environment variable
    :param prefixed whether to add project name prefix to env var or not
    :param default: default value if the environment variable was not set
    :return: value of the given environment variable
    """
    key = _PREFIX + name if prefixed else name
    return os.environ.get(key, default)
