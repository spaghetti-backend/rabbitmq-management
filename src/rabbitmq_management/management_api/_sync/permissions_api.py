from rabbitmq_management import http_clients
from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class TopicPermissionsAPI(BaseAPI):
    """
    Managing topic-based permissions for users in specific virtual hosts.
    """

    def all(self) -> list[dict]:
        """List all topic permissions across the cluster."""
        return self._http_client.get(Paths.permissions.topic.all())

    def detail(self, vhost: str, user: str) -> dict:
        """Get topic permissions for a specific user and virtual host."""
        return self._http_client.get(
            Paths.permissions.topic.individual(vhost=vhost, username=user)
        )

    def set(self, vhost: str, user: str, value: dict) -> dict:
        """
        Create or update topic permissions for a user.

        Args:
            value: A dict with mandatory 'exchange', 'write', and 'read' (regex
                strings)
        """
        return self._http_client.put(
            Paths.permissions.topic.individual(vhost=vhost, username=user),
            payload=value,
        )

    def delete(self, vhost: str, user: str) -> dict:
        """Delete topic permissions for a specific user and virtual host."""
        return self._http_client.delete(
            Paths.permissions.topic.individual(vhost=vhost, username=user)
        )


class AsyncPermissionsAPI(BaseAPI):
    """
    Managing standard user permissions and access to topic-based permissions.
    """

    def __init__(self, http_client: http_clients.HTTPClient) -> None:
        super().__init__(http_client)
        self.topic = TopicPermissionsAPI(self._http_client)

    def all(self) -> list[dict]:
        """List all standard user permissions in the cluster."""
        return self._http_client.get(Paths.permissions.all())

    def detail(self, vhost: str, user: str) -> dict:
        """Get standard permissions for a specific user and virtual host."""
        return self._http_client.get(
            Paths.permissions.individual(vhost=vhost, username=user)
        )

    def set(self, vhost: str, user: str, value: dict) -> dict:
        """
        Create or update standard permissions for a user.

        Args:
            value: A dict with mandatory 'configure', 'write', and 'read' (regex
                strings)
        """
        return self._http_client.put(
            Paths.permissions.individual(vhost=vhost, username=user), payload=value
        )

    def delete(self, vhost: str, user: str) -> dict:
        """Delete standard permissions for a specific user and virtual host."""
        return self._http_client.delete(
            Paths.permissions.individual(vhost=vhost, username=user)
        )
