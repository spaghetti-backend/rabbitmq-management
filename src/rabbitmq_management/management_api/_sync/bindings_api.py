from typing import Any, Optional

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class BindingsAPI(BaseAPI):
    """
    Managing RabbitMQ bindings between exchanges and queues/exchanges.
    """

    def all(self) -> list[dict]:
        """List all bindings in the cluster."""
        return self._http_client.get(Paths.bindings.all())

    def by_vhost(self, vhost: str) -> list[dict]:
        """List all bindings in a specific virtual host."""
        return self._http_client.get(Paths.bindings.by_vhost(vhost))

    def exchange_to_queue(self, vhost: str, exchange: str, queue: str) -> list[dict]:
        """List all bindings between a specific exchange and a queue."""
        return self._http_client.get(
            Paths.bindings.exchange_to_queue(
                vhost=vhost, exchange=exchange, queue=queue
            )
        )

    def bind_exchange_to_queue(
        self,
        vhost: str,
        exchange: str,
        queue: str,
        *,
        routing_key: Optional[str] = None,
        arguments: Optional[dict] = None,
    ) -> str:
        """
        Create a binding between an exchange and a queue.

        Returns: 'location' URI of the new binding.
        """
        payload: dict[str, Any] = {}
        if routing_key:
            payload["routing_key"] = routing_key
        if arguments:
            payload["arguments"] = arguments

        path = Paths.bindings.exchange_to_queue(
            vhost=vhost, exchange=exchange, queue=queue
        )
        response = self._http_client.post(path=path, payload=payload)
        return response["headers"]["location"]

    def exchange_to_queue_binding_details(
        self, vhost: str, exchange: str, queue: str, properties_key: str
    ) -> dict:
        """
        Get details of a specific exchange-to-queue binding.

        Args:
            properties_key: Unique binding ID (routing_key + args hash) from the
                bindings list.
        """
        return self._http_client.get(
            Paths.bindings.exchange_to_queue(
                vhost=vhost, exchange=exchange, queue=queue, props=properties_key
            )
        )

    def unbind_exchange_from_queue(
        self, vhost: str, exchange: str, queue: str, properties_key: str
    ) -> dict:
        """
        Delete a binding between an exchange and a queue using its properties_key.

        Args:
            properties_key: Unique binding ID (routing_key + args hash) from the
                bindings list.
        """
        return self._http_client.delete(
            Paths.bindings.exchange_to_queue(
                vhost=vhost, exchange=exchange, queue=queue, props=properties_key
            )
        )

    def exchange_to_exchange(
        self, vhost: str, source: str, destination: str
    ) -> list[dict]:
        """List all bindings between two exchanges."""
        return self._http_client.get(
            Paths.bindings.exchange_to_exchange(
                vhost=vhost, source=source, destination=destination
            )
        )

    def bind_exchange_to_exchange(
        self,
        vhost: str,
        source: str,
        destination: str,
        *,
        routing_key: Optional[str] = None,
        arguments: Optional[dict] = None,
    ) -> str:
        """
        Create a binding between two exchanges.

        Returns: 'location' URI of the new binding.
        """
        payload: dict[str, Any] = {}
        if routing_key:
            payload["routing_key"] = routing_key
        if arguments:
            payload["arguments"] = arguments

        path = Paths.bindings.exchange_to_exchange(
            vhost=vhost, source=source, destination=destination
        )
        response = self._http_client.post(path=path, payload=payload)
        return response["headers"]["location"]

    def exchange_to_exchange_binding_details(
        self, vhost: str, source: str, destination: str, properties_key: str
    ) -> dict:
        """
        Get details of a specific exchange-to-exchange binding.

        Args:
            properties_key: Unique binding ID (routing_key + args hash) from the
                bindings list.
        """
        return self._http_client.get(
            Paths.bindings.exchange_to_exchange(
                vhost=vhost,
                source=source,
                destination=destination,
                props=properties_key,
            )
        )

    def unbind_exchange_from_exchange(
        self, vhost: str, source: str, destination: str, properties_key: str
    ) -> dict:
        """
        Delete a binding between two exchanges using its properties_key.

        Args:
            properties_key: Unique binding ID (routing_key + args hash) from the
                bindings list.
        """
        return self._http_client.delete(
            Paths.bindings.exchange_to_exchange(
                vhost=vhost,
                source=source,
                destination=destination,
                props=properties_key,
            )
        )
