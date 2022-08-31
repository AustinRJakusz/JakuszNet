# Future imports
from __future__ import annotations

# Standard library imports
from os import path as os_path
from pathlib import Path
from sys import path as sys_path
from tomli import load as tomli_load
from typing import TYPE_CHECKING

# 3rd party library imports

# Type Checking
if TYPE_CHECKING:
    from typing import BinaryIO

    from custom_types import TypedDictConfig
    from custom_types import TypedDictDatabaseConfig
    from custom_types import TypedDictDjangoConfig
    from custom_types import TypedDictTemplatesConfig
    from custom_types import TypedDictAuthPasswordValidators

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Path = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
f: BinaryIO
with open('./configs/config.toml', 'rb') as f:
    TOML_CONFIG: TypedDictConfig = tomli_load(f)
    TOML_DJANGO_CONFIG: TypedDictDjangoConfig = TOML_CONFIG['django_settings']
    TOML_DATABASE_CONFIG: TypedDictDatabaseConfig = TOML_CONFIG['database_settings']
    f.close()

SECRET_KEY: str = TOML_DJANGO_CONFIG['secret_key']
# Application definition
sys_path.insert(0, os_path.join(BASE_DIR, 'apps'))

INSTALLED_APPS: tuple[str, ...] = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.core')

MIDDLEWARE: tuple[str, ...] = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware')

ROOT_URLCONF: str = 'JakuszNet.urls'

TEMPLATES: tuple[TypedDictTemplatesConfig] = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages')}},)

WSGI_APPLICATION: str = 'JakuszNet.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS: tuple[TypedDictAuthPasswordValidators, ...] = (
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'})

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE: str = 'en-us'

TIME_ZONE: str = 'UTC'

USE_I18N: bool = True

USE_TZ: bool = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL: str = 'static/'
MEDIA_URL: str = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'
