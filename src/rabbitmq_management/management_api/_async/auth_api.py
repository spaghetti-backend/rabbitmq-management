from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncAuthAPI(BaseAPI):
    async def attempts(self, node: str) -> list[dict]:
        """
        A list of authentication attempts
        """
        return await self._http_client.get(Paths.auth.attempts(node))

    async def reset_attempts(self, node: str) -> dict:
        """
        Reset authentication attempts
        """
        return await self._http_client.delete(Paths.auth.attempts(node))

    async def attempts_by_source(self, node: str) -> list[dict]:
        """
        A list of authentication attempts by remote address and username
        """
        return await self._http_client.get(Paths.auth.attempts_by_source(node))

    async def reset_attempts_by_source(self, node: str) -> dict:
        """
        Reset authentication attempts by remote address and username
        """
        return await self._http_client.delete(Paths.auth.attempts_by_source(node))

    async def detail(self) -> dict:
        """
        Details about the OAuth2 configuration.

        It will return HTTP status 200 with body:
        {
          "oauth_enabled":"boolean",
          "oauth_client_id":"string",
          "oauth_provider_url":"string"
        }
        """
        return await self._http_client.get(Paths.auth.detail())

    async def hash_password(self, password: str) -> dict:
        """
        Hashes plaintext-password according to the currently configured password
        hashing algorithm.
        """
        return await self._http_client.get(Paths.auth.hash_password(password))
