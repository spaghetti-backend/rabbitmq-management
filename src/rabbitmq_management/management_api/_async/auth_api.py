from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncAuthAPI(BaseAPI):
    """
    Managing RabbitMQ authentication mechanisms and security checks.
    """

    async def attempts(self, node: str) -> list[dict]:
        """List of authentication attempts on a specific node."""
        return await self._http_client.get(Paths.auth.attempts(node))

    async def reset_attempts(self, node: str) -> dict:
        """Reset authentication attempts log for a specific node."""
        return await self._http_client.delete(Paths.auth.attempts(node))

    async def attempts_by_source(self, node: str) -> list[dict]:
        """List of authentication attempts grouped by remote address and username."""
        return await self._http_client.get(Paths.auth.attempts_by_source(node))

    async def reset_attempts_by_source(self, node: str) -> dict:
        """Reset authentication attempt statistics by source for a specific node."""
        return await self._http_client.delete(Paths.auth.attempts_by_source(node))

    async def detail(self) -> dict:
        """Get OAuth2 configuration details if enabled."""
        return await self._http_client.get(Paths.auth.detail())

    async def hash_password(self, password: str) -> dict:
        """
        Hash a plaintext password using the node's configured hashing algorithm.
        """
        return await self._http_client.get(Paths.auth.hash_password(password))
