from typing import Optional

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class ConnectionsAPI(BaseAPI):
    """
    Managing RabbitMQ TCP connections.
    """

    def all(self) -> list[dict]:
        """List all open connections in the cluster."""
        return self._http_client.get(Paths.connections.all())

    def by_user(self, username: str) -> list[dict]:
        """List all open connections for a specific user."""
        return self._http_client.get(Paths.connections.by_user(username=username))

    def channels(self, connection: str) -> list[dict]:
        """
        List all channels associated with a specific connection.

        Args:
            connection: The connection name (e.g., '127.0.0.1:54321 -> 127.0.0.1:5672').
        """
        return self._http_client.get(Paths.connections.channels(connection=connection))

    def close(self, connection: str, *, reason: Optional[str] = None) -> dict:
        """
        Forcefully close a specific connection.

        Args:
            reason: Optional string provided to the client via 'X-Reason' header.
        """
        headers = {"X-Reason": reason} if reason is not None else None

        return self._http_client.delete(
            Paths.connections.detail(connection), headers=headers
        )

    def close_user_connections(
        self, username: str, *, reason: Optional[str] = None
    ) -> dict:
        """
        Forcefully close all connections for a specific user.

        Args:
            reason: Optional string provided to the client via 'X-Reason' header.
        """
        headers = {"X-Reason": reason} if reason is not None else None

        return self._http_client.delete(
            Paths.connections.by_user(username=username), headers=headers
        )

    def detail(self, connection: str) -> dict:
        """Get detailed information about an individual connection."""
        return self._http_client.get(Paths.connections.detail(connection=connection))
