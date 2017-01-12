
class UserProfileMixin:
    pass

class UserAuthzMixin:
    is_active = True
    is_staff = True

def get_username(request):
    return "dummy"
