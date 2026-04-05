from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncNodesAPI(BaseAPI):
    """
    Monitoring nodes in the RabbitMQ cluster.
    """

    async def all(self) -> list[dict]:
        """List all nodes in the RabbitMQ cluster."""
        return await self._http_client.get(Paths.nodes.all())

    async def detail(
        self, node: str, *, memory: bool = False, binary: bool = False
    ) -> dict:
        """
        Get detailed information about a specific node.

        Args:
            node: The node name (e.g., 'rabbit@localhost').
            memory: If True, includes detailed memory statistics.
            binary: If True, includes a breakdown of binary memory usage (expensive).
        """
        return await self._http_client.get(
            Paths.nodes.detail(node, memory=memory, binary=binary)
        )
