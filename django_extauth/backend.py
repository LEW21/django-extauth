from importlib import import_module
from django.conf import settings

backend = import_module(settings.EXTAUTH_BACKEND)
