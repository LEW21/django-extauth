import requests

from .settings import *

class UserAuthzMixin:
    @property
    def _data(self):
        try:
            return self._data_cache
        except AttributeError:
            r = requests.get(GITLAB_URL + "/api/v3/users/", params=dict(username=self.username), headers={"PRIVATE-TOKEN": ACCESS_TOKEN})
            r.raise_for_status()
            data = r.json()

            if len(data) != 1:
                if len(data) == 0:
                    return False
                raise ValueError("Multiple users returned by Gitlab, something is very wrong with the username and/or Gitlab.")
            self._data_cache = data[0]

            return self._data_cache

    @property
    def is_active(self):
        return self._data["state"] == "active"

    @property
    def is_staff(self):
        return self._data["is_admin"] == True
