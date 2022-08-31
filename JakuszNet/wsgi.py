# Standard imports
from os import environ as os_environ
from typing import TYPE_CHECKING

# 3rd party imports
from django.core.wsgi import get_wsgi_application

# Type checking
if TYPE_CHECKING:
    from django.core.wsgi import WSGIHandler

os_environ.setdefault('DJANGO_SETTINGS_MODULE', 'JakuszNet.settings.settings_dev')

application: WSGIHandler = get_wsgi_application()
