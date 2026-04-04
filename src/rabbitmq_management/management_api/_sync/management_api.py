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


class RMQManagementAPI:
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
        self._http_client = http_clients.HTTPClient(
            api_url=f"{api_url}/api/",
            username=username,
            password=password,
            timeout=timeout,
            verify=verify,
            cert=cert,
        )
        self.auth = auth_api.AuthAPI(self._http_client)
        self.bindings = bindings_api.BindingsAPI(self._http_client)
        self.channels = channels_api.ChannelsAPI(self._http_client)
        self.connections = connections_api.ConnectionsAPI(self._http_client)
        self.consumers = consumers_api.ConsumersAPI(self._http_client)
        self.definitions = definitions_api.DefinitionsAPI(self._http_client)
        self.exchanges = exchanges_api.ExchangesAPI(self._http_client)
        self.health = health_api.AsyncHealthAPI(self._http_client)
        self.nodes = nodes_api.NodesAPI(self._http_client)
        self.parameters = parameters_api.ParametersAPI(self._http_client)
        self.permissions = permissions_api.AsyncPermissionsAPI(self._http_client)
        self.policies = policies_api.PoliciesAPI(self._http_client)
        self.queues = queues_api.QueuesAPI(self._http_client)
        self.users = users_api.UsersAPI(self._http_client)
        self.vhosts = vhosts_api.VHostsAPI(self._http_client)

    def __enter__(self) -> RMQManagementAPI:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException],
        exc: BaseException,
        tb: TracebackType,
    ) -> None:
        self.close()

    def aliveness_test(self, vhost: str) -> dict:
        """
        Declares a test queue on the target node,
        then publishes and consumes a message.

        Intended to be used as a very basic health check.

        Responds a 200 OK if the check succeeded,
        otherwise responds with a 503 Service Unavailable.
        """
        return self._http_client.get(Paths.aliveness_test(vhost))

    def cluster_name(self) -> dict:
        """
        Name identifying this RabbitMQ cluster.
        """
        return self._http_client.get(Paths.cluster_name())

    def change_cluster_name(self, name: str) -> dict:
        """
        Change the name identifying this RabbitMQ cluster.
        """
        return self._http_client.put(Paths.cluster_name(), {"name": name})

    def extensions(self) -> list[dict]:
        """
        A list of extensions to the management plugin.
        """
        return self._http_client.get(Paths.extensions())

    def overview(self) -> dict:
        """
        Various random bits of information that describe the whole system.
        """
        return self._http_client.get(Paths.overview())

    def rebalance_queues(self) -> dict:
        """
        Rebalances all queues in all vhosts.

        This operation is asynchronous therefore please check
        the RabbitMQ log file for messages regarding
        the success or failure of the operation.
        """
        return self._http_client.post(Paths.rebalance_queues())

    def whoami(self) -> dict:
        """
        Details of the currently authenticated user.
        """
        return self._http_client.get(Paths.whoami())

    def close(self) -> None:
        self._http_client.close()
