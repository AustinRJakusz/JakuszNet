# Standard imports
from typing import TYPE_CHECKING

# 3rd party imports
from django.contrib import admin
from django.urls import path

if TYPE_CHECKING:
    from django.urls.conf import partial

urlpatterns: tuple[partial, ...] = (
    path('admin/', admin.site.urls),)
