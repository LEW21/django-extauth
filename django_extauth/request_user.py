from .backend import backend
from .models import User

class UserAuthzBase:
    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        """
        if not self.is_active:
            return False
        return self.is_staff

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the specified permission. If an object is
        provided, permissions for this specific object are checked.
        """
        return self.has_module_perms(perm[:perm.index('.')])

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        return all(self.has_perm(perm, obj) for perm in perm_list)

class RequestUser(User, UserAuthzBase, backend.UserAuthzMixin):
    class Meta:
        proxy = True
