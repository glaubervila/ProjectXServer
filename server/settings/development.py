# noinspection PyUnresolvedReferences
from server.settings.defaults import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'adminadmin',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'etc/mysql/my.cnf'),
        }
    }
}
