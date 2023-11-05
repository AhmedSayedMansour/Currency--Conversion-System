import os
from datetime import timedelta
from os.path import join
from pathlib import Path

import yaml

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", "3x*(qu!b9%w^)$(^o+v@y8svs3fmj(10z6mudssp0mibl4lr&3")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", False)

# allow all hosts during development
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1").split(",")

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "http://127.0.0.1").split(",")

# Application definition

INSTALLED_APPS = [
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "watchman",
    "currency_conversion",
    "django_q",
    "django_prometheus",
    "user_management",
    "drf_spectacular",
    'drf_spectacular_sidecar',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

ROOT_URLCONF = "base.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "apps/website/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

WSGI_APPLICATION = "base.wsgi.application"

MIGRATION_MODULES = {
    #'django.contrib.auth' : 'user_management.auth_migrations',
    #'user_management' : 'user_management.auth_migrations',
    #'myapp': 'myapp.migrations'  # this line is only to clarify. IT'S NOT NEEDED AT ALL 
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LOGGER
with open(join(os.getcwd(), "logging.yml"), "r") as f:
    import logging.config

    logging.basicConfig(level=logging.INFO)
    logging.config.dictConfig(yaml.safe_load(f.read()))

# session expiration
SESSION_COOKIE_AGE = 60 * 60  # 1h
# Update the session validity deadline each request
SESSION_SAVE_EVERY_REQUEST = True
# Turn off the browser, then cookie failed
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Static
STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# JWT Auth settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# drf-spectacular documentation settings
SPECTACULAR_SETTINGS = {
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'TITLE': 'RDI Label Studio',
    'DESCRIPTION': 'RDAS',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX': '/api/',
    # OTHER SETTINGS
}

# Authentication
SOCIAL_SECRET_PASSWORD = ' '
USER_EMAIL_ACTIVATION = 'http://127.0.0.1:8000/api/user/activate/<uuid>/<token>/'
USER_PASSWORD_RESET = 'http://127.0.0.1:8000/api/user/reset_password/<uuid>/<token>/'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST = 'smtp.sendgrid.net'
# put your email and password here
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 60 * 60 * 12   # 12h

#allow cors
CORS_ORIGIN_ALLOW_ALL = True

#admin
ADMIN_SITE_HEADER = "Currency-Convertion-System"
# SIMPLEUI_LOGO = "/static/logo.png"
ADMIN_SITE_TITLE = "currency-convertion-system"
# SIMPLEUI_INDEX = 'company-website'
# SIMPLEUI_HOME_TITLE = 'currency-convertion-system'

ASGI_APPLICATION = 'base.asgi.application'

DATA_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # your size limit in bytes


# storage

STORAGES = {
    "default": {
        "BACKEND": "base.utils.custom_storages.CustomFileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
