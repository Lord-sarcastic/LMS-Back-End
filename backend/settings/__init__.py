import django_on_heroku

from .base import *
from .production import *

LOCALS_EXIST = 'Local settings found, overriding production settings...'
LOCALS_NOT_EXIST = 'Local settings not found, using production settings...'
try:
    from .local_settings import *
    print(LOCALS_EXIST)
except ImportError:
    print(LOCALS_NOT_EXIST)

django_on_heroku.settings(locals())
