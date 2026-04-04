from typing import Optional

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class ConnectionsAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of all open connections.
        """
        return self._http_client.get(Paths.connections.all())

    def by_user(self, username: str) -> list[dict]:
        """
        A list of all open connections for a specific username.
        """
        return self._http_client.get(Paths.connections.by_user(username=username))

    def channels(self, connection: str) -> list[dict]:
        """
        List of all channels for a given connection.
        """
        return self._http_client.get(Paths.connections.channels(connection=connection))

    def close(self, connection: str, *, reason: Optional[str] = None) -> dict:
        """
        Close the connection.

        Optionally set the 'reason' to provide a reason.
        """
        headers = {"X-Reason": reason} if reason is not None else None

        return self._http_client.delete(
            Paths.connections.detail(connection), headers=headers
        )

    def close_user_connections(
        self, username: str, *, reason: Optional[str] = None
    ) -> dict:
        """
        Close all the connections for a username.

        Optionally set the 'reason' to provide a reason.
        """
        headers = {"X-Reason": reason} if reason is not None else None

        return self._http_client.delete(
            Paths.connections.by_user(username=username), headers=headers
        )

    def detail(self, connection: str) -> dict:
        """
        An individual connection detailed information.
        """
        return self._http_client.get(Paths.connections.detail(connection=connection))
