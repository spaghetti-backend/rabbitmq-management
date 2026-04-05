from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class DefinitionsAPI(BaseAPI):
    """
    Import and export of RabbitMQ server definitions.
    """

    def all(self) -> dict:
        """
        Export all server definitions (exchanges, queues, users, vhosts, etc.).
        """
        return self._http_client.get(Paths.definitions.all())

    def by_vhost(self, vhost: str) -> dict:
        """
        Export server definitions for a specific virtual host.
        """
        return self._http_client.get(Paths.definitions.by_vhost(vhost=vhost))

    def upload(self, definitions: dict) -> dict:
        """
        Upload and merge a set of server definitions.

        Note:
            Immutable objects (exchanges, queues) are ignored if they conflict.
            Mutable objects are overwritten.
        """
        return self._http_client.post(Paths.definitions.all(), payload=definitions)

    def upload_vhosts_definitions(self, vhost: str, definitions: dict) -> dict:
        """
        Upload and merge definitions for a specific virtual host.

        Note:
            Immutable objects (exchanges, queues) are ignored if they conflict.
            Mutable objects are overwritten.
        """
        return self._http_client.post(
            Paths.definitions.by_vhost(vhost=vhost), payload=definitions
        )
