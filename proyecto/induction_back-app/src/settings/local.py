from .base import *
from .config.debug_toolbar import *


DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',    # https://django-debug-toolbar.readthedocs.io/en/latest/
    'eq_dj_test_back',  # https://pypi.org/project/eq-dj-test-back/
    'django_extensions',  # https://django-extensions.readthedocs.io/
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE