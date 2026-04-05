from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncChannelsAPI(BaseAPI):
    """
    Managing RabbitMQ channels (open AMQP connections over a single TCP socket).
    """

    async def all(self) -> list[dict]:
        """List all open channels in the cluster."""
        return await self._http_client.get(Paths.channels.all())

    async def detail(self, channel: str) -> dict:
        """
        Get details of a specific channel.

        Args:
            channel: The channel name (e.g., '127.0.0.1:54321 -> 127.0.0.1:5672 (1)').
        """
        return await self._http_client.get(Paths.channels.detail(channel=channel))
