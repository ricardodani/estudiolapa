from .settings import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/estudiolapa/data.db',
    }
}

STATIC_ROOT = '/tmp/estudiolapa/static'
MEDIA_ROOT = '/tmp/estudiolapa/media'
