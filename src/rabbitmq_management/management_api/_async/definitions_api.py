from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncDefinitionsAPI(BaseAPI):
    """
    Import and export of RabbitMQ server definitions.
    """

    async def all(self) -> dict:
        """
        Export all server definitions (exchanges, queues, users, vhosts, etc.).
        """
        return await self._http_client.get(Paths.definitions.all())

    async def by_vhost(self, vhost: str) -> dict:
        """
        Export server definitions for a specific virtual host.
        """
        return await self._http_client.get(Paths.definitions.by_vhost(vhost=vhost))

    async def upload(self, definitions: dict) -> dict:
        """
        Upload and merge a set of server definitions.

        Note:
            Immutable objects (exchanges, queues) are ignored if they conflict.
            Mutable objects are overwritten.
        """
        return await self._http_client.post(
            Paths.definitions.all(), payload=definitions
        )

    async def upload_vhosts_definitions(self, vhost: str, definitions: dict) -> dict:
        """
        Upload and merge definitions for a specific virtual host.

        Note:
            Immutable objects (exchanges, queues) are ignored if they conflict.
            Mutable objects are overwritten.
        """
        return await self._http_client.post(
            Paths.definitions.by_vhost(vhost=vhost), payload=definitions
        )
