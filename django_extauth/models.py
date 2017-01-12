from django.db import models
from django.utils.translation import ugettext_lazy as _

from .backend import backend

class UserManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

class User(models.Model, backend.UserProfileMixin):
    objects = UserManager()

    is_anonymous = False
    is_authenticated = True

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def get_username(self):
        "Return the identifying username for this User"
        return getattr(self, self.USERNAME_FIELD)

    def natural_key(self):
        return (self.get_username(),)

    def __str__(self):
        return self.get_username()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        editable=False,
    )
    last_login = models.DateTimeField(_('last login'), blank=True, null=True, editable=False)
