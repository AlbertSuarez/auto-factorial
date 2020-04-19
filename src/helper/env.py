import os

from src.helper import log
from src.config import ENV_NAME_DEVELOPMENT_MODE, ENV_NAME_FACTORIAL_EMAIL_ADDRESS, ENV_NAME_FACTORIAL_PASSWORD, \
    ENV_NAME_START_HOUR, ENV_DEFAULT_START_HOUR


def _get(env_key):
    if env_key in os.environ:
        return os.environ[env_key]
    return None


def is_development():
    return bool(_get(ENV_NAME_DEVELOPMENT_MODE) == 'true')


def get_factorial_email_address():
    return _get(ENV_NAME_FACTORIAL_EMAIL_ADDRESS)


def get_factorial_password():
    return _get(ENV_NAME_FACTORIAL_PASSWORD)


def get_start_hour():
    environment_value = _get(ENV_NAME_START_HOUR)
    if environment_value is not None:
        if environment_value.isdigit() and 0 <= int(environment_value) <= 23:
            return environment_value
        else:
            log.warn(
                f'[{ENV_NAME_START_HOUR}] environment value has to be a natural between 0 and 23. '
                f'Using default value: [{ENV_DEFAULT_START_HOUR}]'
            )
    return ENV_DEFAULT_START_HOUR
