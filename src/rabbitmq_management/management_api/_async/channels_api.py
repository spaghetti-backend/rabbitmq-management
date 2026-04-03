from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncChannelsAPI(BaseAPI):
    async def all(self) -> list[dict]:
        """
        A list of all open channels. Use pagination parameters to filter channels
        """
        return await self._http_client.get(Paths.channels.all())

    async def detail(self, channel: str) -> dict:
        """
        Details about an individual channel
        """
        return await self._http_client.get(Paths.channels.detail(channel=channel))
