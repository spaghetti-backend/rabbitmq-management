from rabbitmq_management import http_clients
from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncTopicPermissionsAPI(BaseAPI):
    async def all(self) -> list[dict]:
        """
        A list of all topic permissions for all users.
        """
        return await self._http_client.get(Paths.permissions.topic.all())

    async def detail(self, vhost: str, user: str) -> dict:
        """
        Topic permissions for a user and virtual host.
        """
        return await self._http_client.get(
            Paths.permissions.topic.individual(vhost=vhost, username=user)
        )

    async def set(self, vhost: str, user: str, value: dict) -> dict:
        """
        To set a topic permission, you will need a 'value' looking something like this:

        {
          "exchange": "amq.topic",
          "write": "^a",
          "read": ".*"
        }

        All keys are mandatory.
        """
        return await self._http_client.put(
            Paths.permissions.topic.individual(vhost=vhost, username=user),
            payload=value,
        )

    async def delete(self, vhost: str, user: str) -> dict:
        """
        Delete topic permission of a user and virtual host.
        """
        return await self._http_client.delete(
            Paths.permissions.topic.individual(vhost=vhost, username=user)
        )


class AsyncPermissionsAPI(BaseAPI):
    def __init__(self, http_client: http_clients.AsyncHTTPClient) -> None:
        super().__init__(http_client)
        self.topic = AsyncTopicPermissionsAPI(self._http_client)

    async def all(self) -> list[dict]:
        """
        A list of all permissions for all users.
        """
        return await self._http_client.get(Paths.permissions.all())

    async def detail(self, vhost: str, user: str) -> dict:
        """
        An individual permission of a user and virtual host.
        """
        return await self._http_client.get(
            Paths.permissions.individual(vhost=vhost, username=user)
        )

    async def set(self, vhost: str, user: str, value: dict) -> dict:
        """
        To set a permission, you will need a 'value' looking something like this:

        {
          "configure": ".*",
          "write": ".*",
          "read": ".*"
        }

        All keys are mandatory.
        """
        return await self._http_client.put(
            Paths.permissions.individual(vhost=vhost, username=user), payload=value
        )

    async def delete(self, vhost: str, user: str) -> dict:
        """
        Delete permission of a user and virtual host.
        """
        return await self._http_client.delete(
            Paths.permissions.individual(vhost=vhost, username=user)
        )
