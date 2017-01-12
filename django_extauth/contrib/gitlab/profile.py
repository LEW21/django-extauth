from .settings import *

class UserProfileMixin:
    def get_absolute_url(self):
        return GITLAB_URL + "/" + self.username
