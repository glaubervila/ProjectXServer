print("Using Settings Travis")

# BASE_PROJECT = os.environ.get("TRAVIS_BUILD_DIR")
# print("BaseProject %s" % BASE_PROJECT)

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
