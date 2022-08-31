# Future imports
from __future__ import annotations

# Standard library imports
from typing import TYPE_CHECKING

# Local imports
from .settings_common import AUTH_PASSWORD_VALIDATORS
from .settings_common import BASE_DIR
from .settings_common import DEFAULT_AUTO_FIELD
from .settings_common import INSTALLED_APPS
from .settings_common import LANGUAGE_CODE
from .settings_common import MEDIA_URL
from .settings_common import MIDDLEWARE
from .settings_common import ROOT_URLCONF
from .settings_common import SECRET_KEY
from .settings_common import STATIC_URL
from .settings_common import TEMPLATES
from .settings_common import TIME_ZONE
from .settings_common import TOML_DATABASE_CONFIG
from .settings_common import USE_I18N
from .settings_common import USE_TZ
from .settings_common import WSGI_APPLICATION

# Type Checking
if TYPE_CHECKING:
    from pathlib import Path

    from custom_types import TypedDictDatabaseSettingsConfig
    from custom_types import TypedDictTemplatesConfig
    from custom_types import TypedDictAuthPasswordValidators

# DO NOT EDIT THIS BLOCK IN THIS FILE, EDIT IN settings_common.py INSTEAD
AUTH_PASSWORD_VALIDATORS: tuple[TypedDictAuthPasswordValidators, ...] = AUTH_PASSWORD_VALIDATORS
BASE_DIR: Path = BASE_DIR
DEFAULT_AUTO_FIELD: str = DEFAULT_AUTO_FIELD
INSTALLED_APPS: tuple[str, ...] = INSTALLED_APPS
LANGUAGE_CODE: str = LANGUAGE_CODE
MIDDLEWARE: tuple[str, ...] = MIDDLEWARE
MEDIA_URL: str = MEDIA_URL
ROOT_URLCONF: str = ROOT_URLCONF
SECRET_KEY: str = SECRET_KEY
STATIC_URL: str = STATIC_URL
TEMPLATES: tuple[TypedDictTemplatesConfig, ...] = TEMPLATES
TIME_ZONE: str = TIME_ZONE
USE_I18N: bool = USE_I18N
USE_TZ: bool = USE_TZ
WSGI_APPLICATION: str = WSGI_APPLICATION
# END DO NOT EDIT

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = True

ALLOWED_HOSTS: tuple[str, ...] = ('*',)

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES: TypedDictDatabaseSettingsConfig = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': TOML_DATABASE_CONFIG['name'],
        'USER': TOML_DATABASE_CONFIG['user'],
        'PASSWORD': TOML_DATABASE_CONFIG['password'],
        'HOST': TOML_DATABASE_CONFIG['host'],
        'PORT': TOML_DATABASE_CONFIG['port']}}
