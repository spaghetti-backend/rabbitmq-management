from rabbitmq_management import http_clients
from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncTopicPermissionsAPI(BaseAPI):
    """
    Managing topic-based permissions for users in specific virtual hosts.
    """

    async def all(self) -> list[dict]:
        """List all topic permissions across the cluster."""
        return await self._http_client.get(Paths.permissions.topic.all())

    async def detail(self, vhost: str, user: str) -> dict:
        """Get topic permissions for a specific user and virtual host."""
        return await self._http_client.get(
            Paths.permissions.topic.individual(vhost=vhost, username=user)
        )

    async def set(self, vhost: str, user: str, value: dict) -> dict:
        """
        Create or update topic permissions for a user.

        Args:
            value: A dict with mandatory 'exchange', 'write', and 'read' (regex
                strings)
        """
        return await self._http_client.put(
            Paths.permissions.topic.individual(vhost=vhost, username=user),
            payload=value,
        )

    async def delete(self, vhost: str, user: str) -> dict:
        """Delete topic permissions for a specific user and virtual host."""
        return await self._http_client.delete(
            Paths.permissions.topic.individual(vhost=vhost, username=user)
        )


class AsyncPermissionsAPI(BaseAPI):
    """
    Managing standard user permissions and access to topic-based permissions.
    """

    def __init__(self, http_client: http_clients.AsyncHTTPClient) -> None:
        super().__init__(http_client)
        self.topic = AsyncTopicPermissionsAPI(self._http_client)

    async def all(self) -> list[dict]:
        """List all standard user permissions in the cluster."""
        return await self._http_client.get(Paths.permissions.all())

    async def detail(self, vhost: str, user: str) -> dict:
        """Get standard permissions for a specific user and virtual host."""
        return await self._http_client.get(
            Paths.permissions.individual(vhost=vhost, username=user)
        )

    async def set(self, vhost: str, user: str, value: dict) -> dict:
        """
        Create or update standard permissions for a user.

        Args:
            value: A dict with mandatory 'configure', 'write', and 'read' (regex
                strings)
        """
        return await self._http_client.put(
            Paths.permissions.individual(vhost=vhost, username=user), payload=value
        )

    async def delete(self, vhost: str, user: str) -> dict:
        """Delete standard permissions for a specific user and virtual host."""
        return await self._http_client.delete(
            Paths.permissions.individual(vhost=vhost, username=user)
        )
