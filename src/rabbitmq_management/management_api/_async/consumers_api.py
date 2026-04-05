from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncConsumersAPI(BaseAPI):
    """
    Managing RabbitMQ consumers across the cluster.
    """

    async def all(self) -> list[dict]:
        """List all consumers in the cluster."""
        return await self._http_client.get(Paths.consumers.all())

    async def by_vhost(self, vhost: str) -> list[dict]:
        """List all consumers in a specific virtual host."""
        return await self._http_client.get(Paths.consumers.by_vhost(vhost=vhost))
