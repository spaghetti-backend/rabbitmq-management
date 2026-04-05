from rabbitmq_management.paths import Paths
from rabbitmq_management.paths.const import UserLimitName

from .base_api import BaseAPI


class UsersAPI(BaseAPI):
    """
    Managing RabbitMQ users, their credentials, permissions, and limits.
    """

    def all(self) -> list[dict]:
        """List all users in the cluster."""
        return self._http_client.get(Paths.users.all())

    def without_permissions(self) -> list[dict]:
        """List users who have no access to any virtual host."""
        return self._http_client.get(Paths.users.without_permissions())

    def bulk_delete(self, value: dict) -> None:
        """
        Delete multiple users in a single request.

        Args:
            value: Dict containing the list of users, e.g., {"users": ["u1", "u2"]}.
        """
        return self._http_client.post(Paths.users.bulk_delete(), payload=value)

    def detail(self, user: str) -> dict:
        """Get details for a specific user."""
        return self._http_client.get(Paths.users.detail(username=user))

    def set(self, user: str, value: dict) -> dict:
        """
        Create or update a user.

        Args:
            value: Dict containing 'tags' (mandatory) and either 'password'
                    или 'password_hash'.

        Note:
            Recognized tags include 'administrator', 'monitoring', and 'management'.
        """
        return self._http_client.put(Paths.users.detail(username=user), payload=value)

    def delete(self, user: str) -> dict:
        """Delete a specific user."""
        return self._http_client.delete(Paths.users.detail(username=user))

    def permissions(self, user: str) -> list[dict]:
        """List all standard permissions assigned to the user."""
        return self._http_client.get(Paths.users.permissions(username=user))

    def topic_permissions(self, user: str) -> list[dict]:
        """List all topic permissions assigned to the user."""
        return self._http_client.get(Paths.users.topic_permissions(username=user))

    def limits(self) -> list[dict]:
        """List per-user limits for all users in the system."""
        return self._http_client.get(Paths.users.limits())

    def individual_limits(self, user: str) -> list[dict]:
        """List per-user limits for a specific user."""
        return self._http_client.get(Paths.users.limits(username=user))

    def set_limit(self, user: str, limit: UserLimitName, value: int) -> dict:
        """
        Set a specific limit for a user (e.g., max-connections, max-channels).
        """
        payload = {"value": value}
        return self._http_client.put(
            Paths.users.set_limits(username=user, limit=limit), payload=payload
        )

    def delete_limit(self, user: str, limit: UserLimitName) -> dict:
        """Remove a specific limit for a user."""
        return self._http_client.delete(
            Paths.users.set_limits(username=user, limit=limit)
        )
