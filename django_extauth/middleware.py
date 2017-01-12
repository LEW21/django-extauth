from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils.functional import SimpleLazyObject
from django.utils.module_loading import import_string

from .backend import backend
from .request_user import RequestUser

def get_user(request):
    try:
        return request._cached_user
    except AttributeError:
        username = backend.get_username(request)
        if username:
            request._cached_user, created = RequestUser.objects.get_or_create(username=username)
        else:
            request._cached_user = AnonymousUser()
        return request._cached_user

class AuthenticationMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        try:
            needs_session = backend.needs_session
        except AttributeError:
            needs_session = False

        if needs_session:
            assert hasattr(request, 'session'), (
                "Selected extauth backend requires session middleware "
                "to be installed. Edit your MIDDLEWARE setting to insert "
                "'django.contrib.sessions.middleware.SessionMiddleware' before "
                "'django_extauth.middleware.AuthenticationMiddleware'."
            ).format(name)

        request.user = SimpleLazyObject(lambda: get_user(request))
        return self.get_response(request)
