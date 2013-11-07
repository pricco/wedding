import os

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


def rel(*x):
    return os.path.join(PROJECT_ROOT, *x)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Pablo Ricco', 'pricco@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(PROJECT_ROOT, 'db.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

ALLOWED_HOSTS = ['nataliaypablo.com']


TIME_ZONE = 'America/Montevideo'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True

AWS_ACCESS_KEY_ID = None
AWS_SECRET_ACCESS_KEY = None
AWS_QUERYSTRING_AUTH = False
AWS_IS_GZIPPED = True
AWS_S3_SECURE_URLS = False

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'
MEDIA_BUCKET = 'weddingassets'
MEDIA_HEADERS = {
    'Expires': 'Thu, 31 Dec 2050 00:00:00 GMT',
    'Cache-Control': 'max-age=315360000, public',
}
MEDIA_LOCATION = 'nataliaypablo/media'
MEDIA_DOMAIN = 'd38obarryt175p.cloudfront.net'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

STATIC_ROOT = rel('collectedstatic')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    rel('static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_BUCKET = 'weddingassets'
STATIC_HEADERS = {
    'Expires': 'Thu, 31 Dec 2050 00:00:00 GMT',
    'Cache-Control': 'max-age=315360000, public',
    }
STATIC_LOCATION = 'nataliaypablo/static'
STATIC_DOMAIN = 'd38obarryt175p.cloudfront.net'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

SECRET_KEY = '6lg+yulbm5m=e&8=@e=5j&0r5xqtk(j08*ee8v9*c1b0fz8(ki'

GOOGLE_API_KEY = None

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'core.context_processors.inject_settings'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTH_USER_MODEL = 'account.User'

ROOT_URLCONF = 'wedding.urls'

WSGI_APPLICATION = 'wedding.wsgi.application'

TEMPLATE_DIRS = (
    rel('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'south',

    'core',
    'account',
    'home',
    'music',
    'location',
    'rsvp',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from settings_local import *
except ImportError:
    pass