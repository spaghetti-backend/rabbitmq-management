from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncConsumersAPI(BaseAPI):
    async def all(self) -> list[dict]:
        """
        A list of all consumers
        """
        return await self._http_client.get(Paths.consumers.all())

    async def by_vhost(self, vhost: str) -> dict:
        """
        A list of all consumers in a given virtual host
        """
        return await self._http_client.get(Paths.consumers.by_vhost(vhost=vhost))
