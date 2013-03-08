import dj_database_url,os

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
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['nataliaypablo.com']


TIME_ZONE = 'America/Montevideo'
LANGUAGE_CODE = 'es-uy'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'
STATIC_ROOT = rel('collectstatic')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    rel('static')
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '6lg+yulbm5m=e&8=@e=5j&0r5xqtk(j08*ee8v9*c1b0fz8(ki'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'wedding.urls'

WSGI_APPLICATION = 'wedding.wsgi.application'

TEMPLATE_DIRS = (
    rel('templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
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