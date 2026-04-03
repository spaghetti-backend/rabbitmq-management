from rabbitmq_management.paths import Paths
from rabbitmq_management.paths.const import VHostLimitName

from .base_api import BaseAPI


class AsyncVHostsAPI(BaseAPI):
    async def all(self) -> list[dict]:
        """
        A list of all vhosts.
        """
        return await self._http_client.get(Paths.vhosts.all())

    async def detail(self, vhost: str) -> dict:
        """
        An individual virtual host.
        """
        return await self._http_client.get(Paths.vhosts.detail(vhost=vhost))

    async def set(self, vhost: str, value: dict) -> dict:
        """
        As a virtual host usually only has a name,
        you do not need an HTTP body when setting one of these.
        To set metadata on creation, provide a body like the following:

        {
          "description": "virtual host description",
          "tags": "accounts,production"
        }

        'tags' is a comma-separated list of tags.
        These metadata fields are optional.

        To enable / disable tracing, provide a body looking like:

        {"tracing":true}
        """
        return await self._http_client.put(
            Paths.vhosts.detail(vhost=vhost), payload=value
        )

    async def delete(self, vhost: str) -> dict:
        """
        Delete the virtual host.
        """
        return await self._http_client.delete(Paths.vhosts.detail(vhost=vhost))

    async def permissions(self, vhost: str) -> list[dict]:
        """
        A list of all permissions for a given virtual host.
        """
        return await self._http_client.get(Paths.vhosts.permissions(vhost=vhost))

    async def topic_permissions(self, vhost: str) -> list[dict]:
        """
        A list of all topic permissions for a given virtual host.
        """
        return await self._http_client.get(Paths.vhosts.topic_permissions(vhost=vhost))

    async def start(self, vhost: str, node: str) -> None:
        """
        Starts virtual host on node.
        """
        return await self._http_client.post(Paths.vhosts.start(vhost=vhost, node=node))

    async def channels(self, vhost: str) -> list[dict]:
        """
        A list of all open channels in a specific virtual host.
        """
        return await self._http_client.get(Paths.vhosts.channels(vhost=vhost))

    async def connections(self, vhost: str) -> list[dict]:
        """
        A list of all open connections in a specific virtual host.
        """
        return await self._http_client.get(Paths.vhosts.connections(vhost=vhost))

    async def limits(self) -> list[dict]:
        """
        Lists per-vhost limits for all vhosts.
        """
        return await self._http_client.get(Paths.vhosts.limits())

    async def vhost_limits(self, vhost: str) -> list[dict]:
        """
        Lists per-vhost limits for specific vhost.
        """
        return await self._http_client.get(Paths.vhosts.limits(vhost=vhost))

    async def set_limit(self, vhost: str, limit: VHostLimitName, value: int) -> dict:
        """
        Set per-vhost limit for vhost.
        """
        payload = {"value": value}
        return await self._http_client.put(
            Paths.vhosts.set_limits(vhost=vhost, limit=limit), payload=payload
        )

    async def delete_limit(self, vhost: str, limit: VHostLimitName) -> dict:
        """
        Delete per-vhost limit for vhost.
        """
        return await self._http_client.delete(
            Paths.vhosts.set_limits(vhost=vhost, limit=limit)
        )
