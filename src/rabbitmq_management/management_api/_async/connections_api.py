from typing import Optional

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncConnectionsAPI(BaseAPI):
    async def all(self) -> list[dict]:
        """
        A list of all open connections.
        """
        return await self._http_client.get(Paths.connections.all())

    async def by_user(self, username: str) -> list[dict]:
        """
        A list of all open connections for a specific username.
        """
        return await self._http_client.get(Paths.connections.by_user(username=username))

    async def channels(self, connection: str) -> list[dict]:
        """
        List of all channels for a given connection.
        """
        return await self._http_client.get(
            Paths.connections.channels(connection=connection)
        )

    async def close(self, connection: str, *, reason: Optional[str] = None) -> dict:
        """
        Close the connection.

        Optionally set the 'reason' to provide a reason.
        """
        headers = {"X-Reason": reason} if reason is not None else None

        return await self._http_client.delete(
            Paths.connections.detail(connection), headers=headers
        )

    async def close_user_connections(
        self, username: str, *, reason: Optional[str] = None
    ) -> dict:
        """
        Close all the connections for a username.

        Optionally set the 'reason' to provide a reason.
        """
        headers = {"X-Reason": reason} if reason is not None else None

        return await self._http_client.delete(
            Paths.connections.by_user(username=username), headers=headers
        )

    async def detail(self, connection: str) -> dict:
        """
        An individual connection detailed information.
        """
        return await self._http_client.get(
            Paths.connections.detail(connection=connection)
        )
