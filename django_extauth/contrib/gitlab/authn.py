from datetime import timedelta
from django.utils import timezone, dateparse
from django_extauth import api
import requests

from .settings import *

needs_session = True

TOKEN_KEY = '_auth_gitlab_token'
EXPIRES_KEY = '_auth_gitlab_expires'

def _get_username(token):
    r = requests.get(GITLAB_URL + "/api/v3/user", params=dict(
        access_token=token,
    ))
    r.raise_for_status()
    data = r.json()
    return data["username"]

def _log_in(request, token, return_path):
    """
    Persist a user id and a backend in the request. This way a user doesn't
    have to reauthenticate on every request. Note that data set during
    the anonymous session is retained when the user logs in.
    """
    res = api.log_in(request, _get_username(token), return_path)

    request.session[TOKEN_KEY] = token
    request.session[EXPIRES_KEY] = (timezone.now() + timedelta(minutes=EXPIRATION_MINUTES)).isoformat()
    
    return res

def get_username(request):
    """
    Returns the user model instance associated with the given request session.
    """
    try:
        token = request.session[TOKEN_KEY]
        expires = dateparse.parse_datetime(request.session[EXPIRES_KEY])
    except KeyError:
        return

    if timezone.now() >= expires:
        return

    return _get_username(token)
