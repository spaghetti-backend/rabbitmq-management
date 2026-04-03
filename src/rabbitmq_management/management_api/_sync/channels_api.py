from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class ChannelsAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of all open channels. Use pagination parameters to filter channels
        """
        return self._http_client.get(Paths.channels.all())

    def detail(self, channel: str) -> dict:
        """
        Details about an individual channel
        """
        return self._http_client.get(Paths.channels.detail(channel=channel))
