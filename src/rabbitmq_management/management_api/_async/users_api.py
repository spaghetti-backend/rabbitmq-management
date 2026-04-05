from rabbitmq_management.paths import Paths
from rabbitmq_management.paths.const import UserLimitName

from .base_api import BaseAPI


class AsyncUsersAPI(BaseAPI):
    """
    Managing RabbitMQ users, their credentials, permissions, and limits.
    """

    async def all(self) -> list[dict]:
        """List all users in the cluster."""
        return await self._http_client.get(Paths.users.all())

    async def without_permissions(self) -> list[dict]:
        """List users who have no access to any virtual host."""
        return await self._http_client.get(Paths.users.without_permissions())

    async def bulk_delete(self, value: dict) -> None:
        """
        Delete multiple users in a single request.

        Args:
            value: Dict containing the list of users, e.g., {"users": ["u1", "u2"]}.
        """
        return await self._http_client.post(Paths.users.bulk_delete(), payload=value)

    async def detail(self, user: str) -> dict:
        """Get details for a specific user."""
        return await self._http_client.get(Paths.users.detail(username=user))

    async def set(self, user: str, value: dict) -> dict:
        """
        Create or update a user.

        Args:
            value: Dict containing 'tags' (mandatory) and either 'password'
                    или 'password_hash'.

        Note:
            Recognized tags include 'administrator', 'monitoring', and 'management'.
        """
        return await self._http_client.put(
            Paths.users.detail(username=user), payload=value
        )

    async def delete(self, user: str) -> dict:
        """Delete a specific user."""
        return await self._http_client.delete(Paths.users.detail(username=user))

    async def permissions(self, user: str) -> list[dict]:
        """List all standard permissions assigned to the user."""
        return await self._http_client.get(Paths.users.permissions(username=user))

    async def topic_permissions(self, user: str) -> list[dict]:
        """List all topic permissions assigned to the user."""
        return await self._http_client.get(Paths.users.topic_permissions(username=user))

    async def limits(self) -> list[dict]:
        """List per-user limits for all users in the system."""
        return await self._http_client.get(Paths.users.limits())

    async def individual_limits(self, user: str) -> list[dict]:
        """List per-user limits for a specific user."""
        return await self._http_client.get(Paths.users.limits(username=user))

    async def set_limit(self, user: str, limit: UserLimitName, value: int) -> dict:
        """
        Set a specific limit for a user (e.g., max-connections, max-channels).
        """
        payload = {"value": value}
        return await self._http_client.put(
            Paths.users.set_limits(username=user, limit=limit), payload=payload
        )

    async def delete_limit(self, user: str, limit: UserLimitName) -> dict:
        """Remove a specific limit for a user."""
        return await self._http_client.delete(
            Paths.users.set_limits(username=user, limit=limit)
        )
