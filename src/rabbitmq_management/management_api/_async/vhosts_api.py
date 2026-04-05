from rabbitmq_management.paths import Paths
from rabbitmq_management.paths.const import VHostLimitName

from .base_api import BaseAPI


class AsyncVHostsAPI(BaseAPI):
    """
    Managing RabbitMQ virtual hosts, including their permissions, limits, and state.
    """

    async def all(self) -> list[dict]:
        """List all virtual hosts in the cluster."""
        return await self._http_client.get(Paths.vhosts.all())

    async def detail(self, vhost: str) -> dict:
        """Get details of a specific virtual host."""
        return await self._http_client.get(Paths.vhosts.detail(vhost=vhost))

    async def set(self, vhost: str, value: dict) -> dict:
        """
        Create a virtual host or update its metadata.

        Args:
            value: Dict with optional keys like 'description', 'tags', or 'tracing'.
        """
        return await self._http_client.put(
            Paths.vhosts.detail(vhost=vhost), payload=value
        )

    async def delete(self, vhost: str) -> dict:
        """Delete a specific virtual host."""
        return await self._http_client.delete(Paths.vhosts.detail(vhost=vhost))

    async def permissions(self, vhost: str) -> list[dict]:
        """List all user permissions for a given virtual host."""
        return await self._http_client.get(Paths.vhosts.permissions(vhost=vhost))

    async def topic_permissions(self, vhost: str) -> list[dict]:
        """List all user topic permissions for a given virtual host."""
        return await self._http_client.get(Paths.vhosts.topic_permissions(vhost=vhost))

    async def start(self, vhost: str, node: str) -> None:
        """Start a virtual host on a specific cluster node."""
        return await self._http_client.post(Paths.vhosts.start(vhost=vhost, node=node))

    async def channels(self, vhost: str) -> list[dict]:
        """List all open channels within a specific virtual host."""
        return await self._http_client.get(Paths.vhosts.channels(vhost=vhost))

    async def connections(self, vhost: str) -> list[dict]:
        """List all active connections to a specific virtual host."""
        return await self._http_client.get(Paths.vhosts.connections(vhost=vhost))

    async def limits(self) -> list[dict]:
        """List resource limits for all virtual hosts."""
        return await self._http_client.get(Paths.vhosts.limits())

    async def vhost_limits(self, vhost: str) -> list[dict]:
        """List resource limits for a specific virtual host."""
        return await self._http_client.get(Paths.vhosts.limits(vhost=vhost))

    async def set_limit(self, vhost: str, limit: VHostLimitName, value: int) -> dict:
        """
        Set a resource limit for a virtual host (e.g., max-queues, max-connections).
        """
        payload = {"value": value}
        return await self._http_client.put(
            Paths.vhosts.set_limits(vhost=vhost, limit=limit), payload=payload
        )

    async def delete_limit(self, vhost: str, limit: VHostLimitName) -> dict:
        """Remove a specific resource limit from a virtual host."""
        return await self._http_client.delete(
            Paths.vhosts.set_limits(vhost=vhost, limit=limit)
        )
