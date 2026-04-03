from rabbitmq_management.paths import Paths
from rabbitmq_management.paths.const import VHostLimitName

from .base_api import BaseAPI


class VHostsAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of all vhosts.
        """
        return self._http_client.get(Paths.vhosts.all())

    def detail(self, vhost: str) -> dict:
        """
        An individual virtual host.
        """
        return self._http_client.get(Paths.vhosts.detail(vhost=vhost))

    def set(self, vhost: str, value: dict) -> dict:
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
        return self._http_client.put(Paths.vhosts.detail(vhost=vhost), payload=value)

    def delete(self, vhost: str) -> dict:
        """
        Delete the virtual host.
        """
        return self._http_client.delete(Paths.vhosts.detail(vhost=vhost))

    def permissions(self, vhost: str) -> list[dict]:
        """
        A list of all permissions for a given virtual host.
        """
        return self._http_client.get(Paths.vhosts.permissions(vhost=vhost))

    def topic_permissions(self, vhost: str) -> list[dict]:
        """
        A list of all topic permissions for a given virtual host.
        """
        return self._http_client.get(Paths.vhosts.topic_permissions(vhost=vhost))

    def start(self, vhost: str, node: str) -> None:
        """
        Starts virtual host on node.
        """
        return self._http_client.post(Paths.vhosts.start(vhost=vhost, node=node))

    def channels(self, vhost: str) -> list[dict]:
        """
        A list of all open channels in a specific virtual host.
        """
        return self._http_client.get(Paths.vhosts.channels(vhost=vhost))

    def connections(self, vhost: str) -> list[dict]:
        """
        A list of all open connections in a specific virtual host.
        """
        return self._http_client.get(Paths.vhosts.connections(vhost=vhost))

    def limits(self) -> list[dict]:
        """
        Lists per-vhost limits for all vhosts.
        """
        return self._http_client.get(Paths.vhosts.limits())

    def vhost_limits(self, vhost: str) -> list[dict]:
        """
        Lists per-vhost limits for specific vhost.
        """
        return self._http_client.get(Paths.vhosts.limits(vhost=vhost))

    def set_limit(self, vhost: str, limit: VHostLimitName, value: int) -> dict:
        """
        Set per-vhost limit for vhost.
        """
        payload = {"value": value}
        return self._http_client.put(
            Paths.vhosts.set_limits(vhost=vhost, limit=limit), payload=payload
        )

    def delete_limit(self, vhost: str, limit: VHostLimitName) -> dict:
        """
        Delete per-vhost limit for vhost.
        """
        return self._http_client.delete(
            Paths.vhosts.set_limits(vhost=vhost, limit=limit)
        )
