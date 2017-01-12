from django.contrib import auth as django_auth
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import urlencode
import requests

from .authn import _log_in
from .settings import *

def login(request):
    return_path = request.GET.get(django_auth.REDIRECT_FIELD_NAME, "")

    return redirect(GITLAB_URL + "/oauth/authorize?" + urlencode(dict(
        client_id=CLIENT_ID,
        redirect_uri=request.build_absolute_uri(reverse("extauth:callback")),
        response_type="code",
        state=return_path,
        scope="read_user",
    )))

def callback(request):
    code = request.GET["code"]
    return_path = request.GET.get("state")

    r = requests.post(GITLAB_URL + "/oauth/token", params=dict(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=request.build_absolute_uri(reverse("extauth:callback")),
        code=code,
        grant_type="authorization_code",
    ))
    r.raise_for_status()
    data = r.json()
    token = data["access_token"]

    return _log_in(request, token, return_path)
