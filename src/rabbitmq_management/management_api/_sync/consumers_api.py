from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class ConsumersAPI(BaseAPI):
    """
    Managing RabbitMQ consumers across the cluster.
    """

    def all(self) -> list[dict]:
        """List all consumers in the cluster."""
        return self._http_client.get(Paths.consumers.all())

    def by_vhost(self, vhost: str) -> list[dict]:
        """List all consumers in a specific virtual host."""
        return self._http_client.get(Paths.consumers.by_vhost(vhost=vhost))
