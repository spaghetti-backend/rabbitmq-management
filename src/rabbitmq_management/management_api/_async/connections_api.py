from typing import Optional

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncConnectionsAPI(BaseAPI):
    """
    Managing RabbitMQ TCP connections.
    """

    async def all(self) -> list[dict]:
        """List all open connections in the cluster."""
        return await self._http_client.get(Paths.connections.all())

    async def by_user(self, username: str) -> list[dict]:
        """List all open connections for a specific user."""
        return await self._http_client.get(Paths.connections.by_user(username=username))

    async def channels(self, connection: str) -> list[dict]:
        """
        List all channels associated with a specific connection.

        Args:
            connection: The connection name (e.g., '127.0.0.1:54321 -> 127.0.0.1:5672').
        """
        return await self._http_client.get(
            Paths.connections.channels(connection=connection)
        )

    async def close(self, connection: str, *, reason: Optional[str] = None) -> dict:
        """
        Forcefully close a specific connection.

        Args:
            reason: Optional string provided to the client via 'X-Reason' header.
        """
        headers = {"X-Reason": reason} if reason is not None else None

        return await self._http_client.delete(
            Paths.connections.detail(connection), headers=headers
        )

    async def close_user_connections(
        self, username: str, *, reason: Optional[str] = None
    ) -> dict:
        """
        Forcefully close all connections for a specific user.

        Args:
            reason: Optional string provided to the client via 'X-Reason' header.
        """
        headers = {"X-Reason": reason} if reason is not None else None

        return await self._http_client.delete(
            Paths.connections.by_user(username=username), headers=headers
        )

    async def detail(self, connection: str) -> dict:
        """Get detailed information about an individual connection."""
        return await self._http_client.get(
            Paths.connections.detail(connection=connection)
        )
