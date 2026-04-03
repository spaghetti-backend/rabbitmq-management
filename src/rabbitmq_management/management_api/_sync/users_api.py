from rabbitmq_management.paths import Paths
from rabbitmq_management.paths.const import UserLimitName

from .base_api import BaseAPI


class UsersAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of all users.
        """
        return self._http_client.get(Paths.users.all())

    def without_permissions(self) -> list[dict]:
        """
        A list of users that do not have access to any virtual host.
        """
        return self._http_client.get(Paths.users.without_permissions())

    def bulk_delete(self, value: dict) -> None:
        """
        Bulk deletes a list of users. Request body must contain the list:

        {"users" : ["user1", "user2", "user3"]}
        """
        return self._http_client.post(Paths.users.bulk_delete(), payload=value)

    def detail(self, user: str) -> dict:
        """
        An individual user.
        """
        return self._http_client.get(Paths.users.detail(username=user))

    def set(self, user: str, value: dict) -> dict:
        """
        To set a user, you will need a body looking something like this:

        {
          "password": "secret",
          "tags": "administrator"
        }

        or:

        {
          "password_hash": "2lmoth8l4H0DViLaK9Fxi6l9ds8=",
          "tags": "administrator"
        }

        The tags key is mandatory.
        Either 'password' or 'password_hash' can be set.
        If neither are set the user will not be able to log in with a password, but
        other mechanisms like client certificates may be used.
        Setting 'password_hash' to "" will ensure the user cannot use a password to log in.
        'tags' is a comma-separated list of tags for the user.
        Currently recognised tags are 'administrator', 'monitoring' and 'management'.
        'password_hash' must be generated using the algorithm described here.
        You may also specify the hash function being used by adding the 'hashing_algorithm' key to the body.
        Currently recognised algorithms are 'rabbit_password_hashing_sha256',
        'rabbit_password_hashing_sha512', and 'rabbit_password_hashing_md5'.
        """
        return self._http_client.put(Paths.users.detail(username=user), payload=value)

    def delete(self, user: str) -> dict:
        """
        Delete the user.
        """
        return self._http_client.delete(Paths.users.detail(username=user))

    def permissions(self, user: str) -> list[dict]:
        """
        A list of all permissions for a given user.
        """
        return self._http_client.get(Paths.users.permissions(username=user))

    def topic_permissions(self, user: str) -> list[dict]:
        """
        A list of all topic permissions for a given user.
        """
        return self._http_client.get(Paths.users.topic_permissions(username=user))

    def limits(self) -> list[dict]:
        """
        Lists per-user limits for all users.
        """
        return self._http_client.get(Paths.users.limits())

    def individual_limits(self, user: str) -> list[dict]:
        """
        Lists per-user limits for a specific user.
        """
        return self._http_client.get(Paths.users.limits(username=user))

    def set_limit(self, user: str, limit: UserLimitName, value: int) -> dict:
        """
        Set per-user limit for user.
        """
        payload = {"value": value}
        return self._http_client.put(
            Paths.users.set_limits(username=user, limit=limit), payload=payload
        )

    def delete_limit(self, user: str, limit: UserLimitName) -> dict:
        """
        Delete per-user limit for user.
        """
        return self._http_client.delete(
            Paths.users.set_limits(username=user, limit=limit)
        )
