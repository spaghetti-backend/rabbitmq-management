from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class NodesAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of nodes in the RabbitMQ cluster.
        """
        return self._http_client.get(Paths.nodes.all())

    def detail(self, node: str, *, memory: bool = False, binary: bool = False) -> dict:
        """
        An individual node in the RabbitMQ cluster.
        Add 'memory=True' to get memory statistics,
        and 'binary=True' to get a breakdown of binary memory use
        (may be expensive if there are many small binaries in the system).
        """
        return self._http_client.get(
            Paths.nodes.detail(node, memory=memory, binary=binary)
        )
