from __future__ import annotations

from typing import TYPE_CHECKING

from rabbitmq_management import http_clients
from rabbitmq_management.paths import Paths

from . import (
    auth_api,
    bindings_api,
    channels_api,
    connections_api,
    consumers_api,
    definitions_api,
    exchanges_api,
    health_api,
    nodes_api,
    parameters_api,
    permissions_api,
    policies_api,
    queues_api,
    users_api,
    vhosts_api,
)

if TYPE_CHECKING:
    import ssl
    from types import TracebackType


class AsyncRMQManagementAPI:
    """
    Client for the RabbitMQ Management HTTP API.

    This class provides a structured interface to manage a RabbitMQ cluster,
    including vhosts, users, exchanges, queues, and health monitoring.
    It supports both manual session management and asynchronous context managers.

    Example:
        ```python
        async with AsyncRMQManagementAPI(
            "http://localhost:15672", "guest", "guest"
        ) as client:
            overview = await client.overview()
        ```
        ```python
        client = AsyncRMQManagementAPI("http://localhost:15672", "guest", "guest")
        overview = await client.overview()
        await client.close()
        ```

    Attributes:
        auth: Authentication and security checks.
        bindings: Exchange and queue bindings management.
        channels: Active AMQP channels monitoring.
        connections: Client TCP connections management.
        consumers: Message consumers monitoring.
        definitions: Import/Export of server definitions.
        exchanges: Exchange management.
        health: Cluster and node health checks.
        nodes: Cluster nodes monitoring.
        parameters: Runtime parameters and federation.
        permissions: User permissions management.
        policies: Runtime policies management.
        queues: Queue management and messaging.
        users: User account management.
        vhosts: Virtual host management.
    """

    def __init__(
        self,
        api_url: str,
        username: str,
        password: str,
        *,
        timeout: float = 5.0,
        verify: ssl.SSLContext | str | bool = True,
        cert: http_clients.CertTypes | None = None,
    ) -> None:
        """
        Initialize the API client and all its sub-resources.
        """
        self._http_client = http_clients.AsyncHTTPClient(
            api_url=f"{api_url}/api/",
            username=username,
            password=password,
            timeout=timeout,
            verify=verify,
            cert=cert,
        )
        self.auth = auth_api.AsyncAuthAPI(self._http_client)
        self.bindings = bindings_api.AsyncBindingsAPI(self._http_client)
        self.channels = channels_api.AsyncChannelsAPI(self._http_client)
        self.connections = connections_api.AsyncConnectionsAPI(self._http_client)
        self.consumers = consumers_api.AsyncConsumersAPI(self._http_client)
        self.definitions = definitions_api.AsyncDefinitionsAPI(self._http_client)
        self.exchanges = exchanges_api.AsyncExchangesAPI(self._http_client)
        self.health = health_api.AsyncHealthAPI(self._http_client)
        self.nodes = nodes_api.AsyncNodesAPI(self._http_client)
        self.parameters = parameters_api.AsyncParametersAPI(self._http_client)
        self.permissions = permissions_api.AsyncPermissionsAPI(self._http_client)
        self.policies = policies_api.AsyncPoliciesAPI(self._http_client)
        self.queues = queues_api.AsyncQueuesAPI(self._http_client)
        self.users = users_api.AsyncUsersAPI(self._http_client)
        self.vhosts = vhosts_api.AsyncVHostsAPI(self._http_client)

    async def __aenter__(self) -> AsyncRMQManagementAPI:
        """Enter the asynchronous context and return the client instance."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException],
        exc: BaseException,
        tb: TracebackType,
    ) -> None:
        """Exit the context and ensure the HTTP session is closed."""
        await self.close()

    async def aliveness_test(self, vhost: str) -> dict:
        """
        Execute a basic health check by publishing and consuming a test message.
        """
        return await self._http_client.get(Paths.aliveness_test(vhost))

    async def cluster_name(self) -> dict:
        """Get the name identifying this RabbitMQ cluster."""
        return await self._http_client.get(Paths.cluster_name())

    async def change_cluster_name(self, name: str) -> dict:
        """Update the cluster name."""
        return await self._http_client.put(Paths.cluster_name(), {"name": name})

    async def extensions(self) -> list[dict]:
        """List all active management plugin extensions."""
        return await self._http_client.get(Paths.extensions())

    async def overview(self) -> dict:
        """Get system-wide information (cluster state, versions, stats)."""
        return await self._http_client.get(Paths.overview())

    async def rebalance_queues(self) -> dict:
        """
        Trigger asynchronous queue rebalancing across all virtual hosts.
        """
        return await self._http_client.post(Paths.rebalance_queues())

    async def whoami(self) -> dict:
        """Get details of the currently authenticated user."""
        return await self._http_client.get(Paths.whoami())

    async def close(self) -> None:
        """Close the underlying HTTP session and release resources."""
        await self._http_client.close()
