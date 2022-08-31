# Future imports
from __future__ import annotations

# Standard library imports
from typing import TYPE_CHECKING
from typing import TypedDict

if TYPE_CHECKING:
    from typing import Type

TypedDictDjangoConfig: Type = TypedDict(
    'TypedDictDjangoConfig', {
        'secret_key': str})

TypedDictDatabaseConfig: Type = TypedDict(
    'TypedDictDatabaseConfig', {
        'name': str,
        'user': str,
        'password': str,
        'host': str,
        'port': str})

TypedDictConfig: Type = TypedDict(
    'TypedDictConfig', {
        'django_settings': TypedDictDjangoConfig,
        'database_settings': TypedDictDatabaseConfig})

TypedDictTemplatesConfigOptions: Type = TypedDict(
    'TypedDictTemplatesConfigOptions', {
        'context_processors': tuple[str, ...]})

TypedDictTemplatesConfig: Type = TypedDict(
    'TypedDictTemplatesConfig', {
        'BACKEND': str,
        'DIRS': tuple[str, ...],
        'APP_DIRS': bool,
        'OPTIONS': TypedDictTemplatesConfigOptions})

TypedDictAuthPasswordValidators: Type = TypedDict(
    'TypedDictAuthPasswordValidators', {
        'NAME': str})

TypedDictDatabaseConfigSQLITE: Type = TypedDict(
    'TypedDictDatabaseConfigSQLITE', {
        'ENGINE': str,
        'NAME': str})

TypedDictDatabaseConfigMYSQL: Type = TypedDict(
    'TypedDictDatabaseConfigMYSQL', {
        'ENGINE': str,
        'NAME': str,
        'USER': str,
        'PASSWORD': str,
        'HOST': str,
        'PORT': str})

TypedDictDatabaseSettingsConfig: Type = TypedDict(
    'TypedDictDatabaseSettingsConfig', {
        'default': TypedDictDatabaseConfigSQLITE | TypedDictDatabaseConfigMYSQL})
