from .backend import backend

app_name = 'extauth'
try:
    urlpatterns = backend.urlpatterns
except AttributeError:
    urlpatterns = []
