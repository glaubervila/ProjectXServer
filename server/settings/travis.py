# noinspection PyUnresolvedReferences
from server.settings.defaults import *

print("Using Settings Travis")

ALLOWED_HOSTS = '*'

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}
