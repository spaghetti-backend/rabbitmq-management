from typing import Any, Optional

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncExchangesAPI(BaseAPI):
    """
    Managing RabbitMQ exchanges.
    """

    async def all(self) -> list[dict]:
        """List all exchanges in the cluster."""
        return await self._http_client.get(Paths.exchanges.all())

    async def by_vhost(self, vhost: str) -> list[dict]:
        """List all exchanges in a specific virtual host."""
        return await self._http_client.get(Paths.exchanges.by_vhost(vhost=vhost))

    async def detail(self, vhost: str, exchange: str) -> dict:
        """Get details of a specific exchange."""
        return await self._http_client.get(
            Paths.exchanges.detail(vhost=vhost, exchange=exchange)
        )

    async def set(
        self,
        vhost: str,
        exchange: str,
        exchange_type: str,
        *,
        auto_delete: Optional[bool] = None,
        durable: Optional[bool] = None,
        internal: Optional[bool] = None,
        arguments: Optional[dict] = None,
    ) -> dict:
        """
        Create or update an exchange.

        Args:
            exchange_type: Type of exchange (e.g., 'direct', 'topic', 'fanout').
            internal: If True, exchange cannot be used directly by publishers.
        """
        payload: dict[str, Any] = {"type": exchange_type}
        if auto_delete is not None:
            payload["auto_delete"] = auto_delete
        if durable is not None:
            payload["durable"] = durable
        if internal is not None:
            payload["internal"] = internal
        if arguments is not None:
            payload["arguments"] = arguments

        return await self._http_client.put(
            Paths.exchanges.detail(vhost=vhost, exchange=exchange), payload=payload
        )

    async def delete(
        self, vhost: str, exchange: str, *, if_unused: bool = False
    ) -> dict:
        """
        Delete an exchange.

        Args:
            if_unused: If True, prevents deletion if the exchange has bindings.
        """
        return await self._http_client.delete(
            Paths.exchanges.detail(vhost=vhost, exchange=exchange, if_unused=if_unused)
        )

    async def source_bindings(self, vhost: str, exchange: str) -> list[dict]:
        """List all bindings where this exchange is the source."""
        return await self._http_client.get(
            Paths.exchanges.source_bindings(vhost=vhost, exchange=exchange)
        )

    async def destination_bindings(self, vhost: str, exchange: str) -> list[dict]:
        """List all bindings where this exchange is the destination."""
        return await self._http_client.get(
            Paths.exchanges.destination_bindings(vhost=vhost, exchange=exchange)
        )
