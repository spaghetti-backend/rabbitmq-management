from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class ConsumersAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of all consumers
        """
        return self._http_client.get(Paths.consumers.all())

    def by_vhost(self, vhost: str) -> dict:
        """
        A list of all consumers in a given virtual host
        """
        return self._http_client.get(Paths.consumers.by_vhost(vhost=vhost))
