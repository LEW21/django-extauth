from django.contrib.auth.signals import user_logged_in
from django.conf import settings
from django.middleware.csrf import rotate_token
from django.shortcuts import redirect, resolve_url
from django.utils.http import is_safe_url

def log_in(request, username, return_path):
    from .request_user import RequestUser

    request.user, created = RequestUser.objects.get_or_create(username=username)
    rotate_token(request)
    user_logged_in.send(sender=request.user.__class__, request=request, user=request.user)

    url_is_safe = is_safe_url(
        url=return_path,
        host=request.get_host(),
        #allowed_hosts=set(request.get_host()),
        #require_https=request.is_secure(),
    )
    if not url_is_safe:
        return redirect(resolve_url(settings.LOGIN_REDIRECT_URL))
    return redirect(return_path)
