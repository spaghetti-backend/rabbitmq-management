from typing import Any, Optional

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class ExchangesAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of all exchanges.
        """
        return self._http_client.get(Paths.exchanges.all())

    def by_vhost(self, vhost: str) -> list[dict]:
        """
        A list of all exchanges in a given virtual host.
        """
        return self._http_client.get(Paths.exchanges.by_vhost(vhost=vhost))

    def detail(self, vhost: str, exchange: str) -> dict:
        """
        An individual exchange.
        """
        return self._http_client.get(
            Paths.exchanges.detail(vhost=vhost, exchange=exchange)
        )

    def create(
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
        Create an exchange.

        The 'type' key is mandatory; other keys are optional.
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

        return self._http_client.put(
            Paths.exchanges.detail(vhost=vhost, exchange=exchange), payload=payload
        )

    def delete(self, vhost: str, exchange: str, *, if_unused: bool = False) -> dict:
        """
        Delete an exchange.

        The if_unused parameter prevents deletion if the exchange is bound to a queue or
        used as a source by another exchange.
        """
        return self._http_client.delete(
            Paths.exchanges.detail(vhost=vhost, exchange=exchange, if_unused=if_unused)
        )

    def source_bindings(self, vhost: str, exchange: str) -> list[dict]:
        """
        A list of all bindings in which a given exchange is the source.
        """
        return self._http_client.get(
            Paths.exchanges.source_bindings(vhost=vhost, exchange=exchange)
        )

    def destination_bindings(self, vhost: str, exchange: str) -> list[dict]:
        """
        A list of all bindings in which a given exchange is the destination.
        """
        return self._http_client.get(
            Paths.exchanges.destination_bindings(vhost=vhost, exchange=exchange)
        )
