"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration


def env(name, default=None):
    return os.environ.get(name, default)


SENTRY_DSN = env(
    "SENTRY_DSN",
    "https://examplePublicKey@o0.ingest.sentry.io/0",
)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration(), CeleryIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
    send_default_pii=False,
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", "not-so-secret")
DEBUG = env("DJANGO_DEBUG", "0") == "1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "django_extensions",
    "graphene_django",
    "corsheaders",
    # 1st party apps
    "backend.core",  # core app should NOT IMPORT any other app
    "backend.questions",
    # "backend.other"  # All other apps should go here
    "backend.contrib",  # contrib app should NOT BE IMPORTED BY any other app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME", default="my_db_name"),
        "USER": env("DATABASE_USER", default="my_username"),
        "PASSWORD": env("DATABASE_PASSWORD", default="my_password"),
        "HOST": env("DATABASE_HOST", default="0.0.0.0"),
        "PORT": env("DATABASE_PORT", default="5432"),
    }
}

if env("USE_SQLITE_DB") == "1":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom Settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = ["GET", "POST", "OPTION"]
CHOICES_JS = "../frontend/src/CHOICES.js"

GRAPHENE = {
    "SCHEMA": "backend.graphql.schema",
    "SCHEMA_OUTPUT": "../frontend/schema.graphql",
    "MIDDLEWARE": [
        "graphene_django.debug.DjangoDebugMiddleware",
    ],
}
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

AWS_EXPIRY = 604700
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", "minioadmin")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", "minioadmin")
AWS_BUCKET_NAME = env("AWS_BUCKET_NAME", "backend-local")
AWS_REGION = env("AWS_REGION", default="us-east-1")
AWS_BUCKET_REGION = env("AWS_BUCKET_REGION", "us-east-1")

# S3? or Minio?
if env("USE_AWS_S3") is None:
    # Use minio
    AWS_S3_ENDPOINT_URL = "http://0.0.0.0:9000"
else:
    # Use AWS S3
    AWS_S3_ENDPOINT_URL = None

UPLOADS_PREFIX = "uploads"

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
FRONTEND_PREFIX = env("FRONTEND_PREFIX", default="http://localhost:3000")

KEYCLOAK_PUBLIC_KEY = env(
    "KEYCLOAK_PUBLIC_KEY",
    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4SvPRqJJA5O//iTg8/+BiCOZB2c0lK8TQ8plfem3md+OFhNC0d21Uzq8PGOSP/BrU/xeqg0DHvlzcriOTC0Zwc+AzEoo+eR+jpeP0isIjUNHz1+sRRVPt69b/+HM331IGkuqTs4qk76ExTD4IMZ3nv0GHsKHZCOanRTSbqQTMaDaW3casXkFQyOYhyEbBu3atFZ+vWtMUkgFJ9wgHSOhWdJkX2JxzR65y/BgiJUtocn7YprKLxEKjHk4b+gLGPE017O81ooInbgH2XcZjxsG/S3Rpw4TSOh/6mpBCYb1YTYT3GzpVCoQ5K1zhe4GgZWLHpPgkKoOVvO7m3+FPXHvWwIDAQAB",  # noqa:E501
)
KEYCLOAK_PUBLIC_KEY = f"""-----BEGIN PUBLIC KEY-----
{KEYCLOAK_PUBLIC_KEY}
-----END PUBLIC KEY-----"""

CELERY_BROKER_URL = env("CELERY_BROKER_URL", "redis://localhost:6379/0")

UPTRACE_DSN = env(
    "UPTRACE_DSN",
    "https://exampleKey@uptrace.dev/0",
)
