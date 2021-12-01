from os import environ

from .base import BASE_DIR

try:
    DEBUG = int(environ.get('DEBUG', 0))
except:
    DEBUG = False

SESSION_COOKIE_DOMAIN = '.' + environ.get('HOST')

CORS_REPLACE_HTTPS_REFERER = True

HOST_SCHEME = "https://"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_SECONDS = 1000000

SECURE_FRAME_DENY = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]


STATIC_ROOT = BASE_DIR / 'static'