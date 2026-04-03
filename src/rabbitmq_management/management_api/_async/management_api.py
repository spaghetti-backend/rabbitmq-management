from __future__ import annotations

from types import TracebackType
from typing import TYPE_CHECKING, Optional, Type, Union

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


class AsyncRMQManagementAPI:
    def __init__(
        self,
        api_url: str,
        username: str,
        password: str,
        *,
        timeout: float = 5.0,
        verify: Union[ssl.SSLContext, str, bool] = True,
        cert: Optional[http_clients.CertTypes] = None,
    ) -> None:
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
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: BaseException,
        tb: TracebackType,
    ) -> None:
        await self.close()

    async def aliveness_test(self, vhost: str) -> dict:
        """
        Declares a test queue on the target node,
        then publishes and consumes a message.

        Intended to be used as a very basic health check.

        Responds a 200 OK if the check succeeded,
        otherwise responds with a 503 Service Unavailable.
        """
        return await self._http_client.get(Paths.aliveness_test(vhost))

    async def cluster_name(self) -> dict:
        """
        Name identifying this RabbitMQ cluster.
        """
        return await self._http_client.get(Paths.cluster_name())

    async def change_cluster_name(self, name: str) -> dict:
        """
        Change the name identifying this RabbitMQ cluster.
        """
        return await self._http_client.put(Paths.cluster_name(), {"name": name})

    async def extensions(self) -> list[dict]:
        """
        A list of extensions to the management plugin.
        """
        return await self._http_client.get(Paths.extensions())

    async def overview(self) -> dict:
        """
        Various random bits of information that describe the whole system.
        """
        return await self._http_client.get(Paths.overview())

    async def rebalance_queues(self) -> dict:
        """
        Rebalances all queues in all vhosts.

        This operation is asynchronous therefore please check
        the RabbitMQ log file for messages regarding
        the success or failure of the operation.
        """
        return await self._http_client.post(Paths.rebalance_queues())

    async def whoami(self) -> dict:
        """
        Details of the currently authenticated user.
        """
        return await self._http_client.get(Paths.whoami())

    async def close(self) -> None:
        await self._http_client.close()
