from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncDefinitionsAPI(BaseAPI):
    async def all(self) -> dict:
        """
        The server definitions - exchanges, queues, bindings, users,
        virtual hosts, permissions, topic permissions, and parameters.

        Everything apart from messages.
        """
        return await self._http_client.get(Paths.definitions.all())

    async def by_vhost(self, vhost: str) -> dict:
        """
        The server definitions for a given virtual host -
        exchanges, queues, bindings and policies.
        """
        return await self._http_client.get(Paths.definitions.by_vhost(vhost=vhost))

    async def upload(self, definitions: dict) -> dict:
        """
        Upload an existing set of definitions.

        Note that:
        - The definitions are merged.
        Anything already existing on the server but not in the uploaded
        definitions is untouched.

        - Conflicting definitions on immutable objects (exchanges, queues and bindings)
        will be ignored. The existing definition will be preserved.

        - Conflicting definitions on mutable objects will cause
        the object in the server to be overwritten with the object from the definitions.

        - In the event of an error you will be left with a part-applied set of definitions.
        """
        return await self._http_client.post(
            Paths.definitions.all(), payload=definitions
        )

    async def upload_vhosts_definitions(self, vhost: str, definitions: dict) -> dict:
        """
        Upload an existing set of definitions.

        Note that:
        - The definitions are merged.
        Anything already existing on the server but not in the uploaded
        definitions is untouched.

        - Conflicting definitions on immutable objects (exchanges, queues and bindings)
        will be ignored. The existing definition will be preserved.

        - Conflicting definitions on mutable objects will cause
        the object in the server to be overwritten with the object from the definitions.

        - In the event of an error you will be left with a part-applied set of definitions.
        """
        return await self._http_client.post(
            Paths.definitions.by_vhost(vhost=vhost), payload=definitions
        )
