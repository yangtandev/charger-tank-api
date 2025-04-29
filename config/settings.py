import os
from pathlib import Path
# import datetime
import environ

# Time Zone
TIME_ZONE = 'Asia/Taipei'
USE_TZ = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(f'{BASE_DIR}/.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qv*o1&&x%#jtsn)5((g+yw#%3_a$ykfof6b-)j^i$1a8se*7c8'
# TODO:import key from the environment

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = [env('ALLOWED_HOST'), ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'debug_toolbar',
    'django_extensions',
    'corsheaders',
    'django_apscheduler',

    # Project apps
    'charger_tank',
    'clientsetting',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': 'postgres',
        'PASSWORD': '87518499',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_FRAMEWORK = {
    # disable PERMISSION & AUTHENTICATION for now.
    # 'DEFAULT_PERMISSION_CLASSES':
    # ('rest_framework.permissions.IsAuthenticated', ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    # )
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10
}

# debug-toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

# test settings
FIXTURE_DIRS = ['fixtures']

# SECURE_SSL_REDIRECT = True

# corsheaders
# CORS_ALLOWED_ORIGINS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

# This scheduler config will:
# - Store jobs in the project database
# - Execute jobs in threads inside the application process
SCHEDULER_CONFIG = {
    "apscheduler.jobstores.default": {
        "class": "django_apscheduler.jobstores:DjangoJobStore"
    },
    'apscheduler.executors.processpool': {
        "type": "threadpool"
    },
}
SCHEDULER_AUTOSTART = True
