from typing import Any, Optional

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncBindingsAPI(BaseAPI):
    async def all(self) -> list[dict]:
        """
        A list of all bindings.
        """
        return await self._http_client.get(Paths.bindings.all())

    async def by_vhost(self, vhost: str) -> list[dict]:
        """
        A list of all bindings in a given virtual host.
        """
        return await self._http_client.get(Paths.bindings.by_vhost(vhost))

    async def exchange_to_queue(
        self, vhost: str, exchange: str, queue: str
    ) -> list[dict]:
        """
        A list of all bindings between an exchange and a queue.

        Remember, an exchange and a queue can be bound together many times!
        """
        return await self._http_client.get(
            Paths.bindings.exchange_to_queue(
                vhost=vhost, exchange=exchange, queue=queue
            )
        )

    async def bind_exchange_to_queue(
        self,
        vhost: str,
        exchange: str,
        queue: str,
        *,
        routing_key: Optional[str] = None,
        arguments: Optional[dict] = None,
    ) -> str:
        """
        Create a new binding.
        Optionally containing two fields, routing_key (a string) and arguments
        (a map of optional arguments):

        routing_key = "my_routing_key"
        arguments = {"x-arg": "value"}

        Return 'location' that telling you the URI of your new binding.
        """
        payload: dict[str, Any] = {}
        if routing_key:
            payload["routing_key"] = routing_key
        if arguments:
            payload["arguments"] = arguments

        path = Paths.bindings.exchange_to_queue(
            vhost=vhost, exchange=exchange, queue=queue
        )
        response = await self._http_client.post(path=path, payload=payload)
        return response["headers"]["location"]

    async def exchange_to_queue_binding_details(
        self, vhost: str, exchange: str, queue: str, properties_key: str
    ) -> dict:
        """
        An individual binding between an exchange and a queue.

        The 'properties_key' part of the URI is a "name" for the binding
        composed of its routing key and a hash of its arguments.

        'properties_key' is the field from a bindings listing response.
        """
        return await self._http_client.get(
            Paths.bindings.exchange_to_queue(
                vhost=vhost, exchange=exchange, queue=queue, props=properties_key
            )
        )

    async def unbind_exchange_from_queue(
        self, vhost: str, exchange: str, queue: str, properties_key: str
    ) -> dict:
        """
        Remove binding between an exchange and a queue.

        The 'properties_key' part of the URI is a "name" for the binding
        composed of its routing key and a hash of its arguments.

        'properties_key' is the field from a bindings listing response.
        """
        return await self._http_client.delete(
            Paths.bindings.exchange_to_queue(
                vhost=vhost, exchange=exchange, queue=queue, props=properties_key
            )
        )

    async def exchange_to_exchange(
        self, vhost: str, source: str, destination: str
    ) -> list[dict]:
        """
        A list of all bindings between two exchanges.
        """
        return await self._http_client.get(
            Paths.bindings.exchange_to_exchange(
                vhost=vhost, source=source, destination=destination
            )
        )

    async def bind_exchange_to_exchange(
        self,
        vhost: str,
        source: str,
        destination: str,
        *,
        routing_key: Optional[str] = None,
        arguments: Optional[dict] = None,
    ) -> str:
        """
        Create a new binding.
        Optionally containing two fields, routing_key (a string) and arguments
        (a map of optional arguments):

        routing_key = "my_routing_key"
        arguments = {"x-arg": "value"}

        Return 'location' that telling you the URI of your new binding.
        """
        payload: dict[str, Any] = {}
        if routing_key:
            payload["routing_key"] = routing_key
        if arguments:
            payload["arguments"] = arguments

        path = Paths.bindings.exchange_to_exchange(
            vhost=vhost, source=source, destination=destination
        )
        response = await self._http_client.post(path=path, payload=payload)
        return response["headers"]["location"]

    async def exchange_to_exchange_binding_details(
        self, vhost: str, source: str, destination: str, properties_key: str
    ) -> dict:
        """
        An individual binding between two exchanges.

        The 'properties_key' part of the URI is a "name" for the binding
        composed of its routing key and a hash of its arguments.

        'properties_key' is the field from a bindings listing response.
        """
        return await self._http_client.get(
            Paths.bindings.exchange_to_exchange(
                vhost=vhost,
                source=source,
                destination=destination,
                props=properties_key,
            )
        )

    async def unbind_exchange_from_exchange(
        self, vhost: str, source: str, destination: str, properties_key: str
    ) -> dict:
        """
        Remove binding between two exchanges.

        The 'properties_key' part of the URI is a "name" for the binding
        composed of its routing key and a hash of its arguments.

        'properties_key' is the field from a bindings listing response.
        """
        return await self._http_client.delete(
            Paths.bindings.exchange_to_exchange(
                vhost=vhost,
                source=source,
                destination=destination,
                props=properties_key,
            )
        )
