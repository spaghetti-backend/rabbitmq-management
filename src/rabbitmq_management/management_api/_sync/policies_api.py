from rabbitmq_management import http_clients
from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class OperatorPoliciesAPI(BaseAPI):
    """
    Managing operator policies (enforced limits that cannot be overridden by users).
    """

    def all(self) -> list[dict]:
        """List all operator policies in the cluster."""
        return self._http_client.get(Paths.operator_policies.all())

    def by_vhost(self, vhost: str) -> list[dict]:
        """List all operator policies in a specific virtual host."""
        return self._http_client.get(Paths.operator_policies.by_vhost(vhost=vhost))

    def detail(self, vhost: str, policy: str) -> dict:
        """Get details of an individual operator policy."""
        return self._http_client.get(
            Paths.operator_policies.detail(vhost=vhost, policy=policy)
        )

    def set(self, vhost: str, policy: str, value: dict) -> dict:
        """
        Create or update an operator policy.

        Args:
            value: Dict with 'pattern' and 'definition' (mandatory),
                   plus 'priority' and 'apply-to' (optional).
        """
        return self._http_client.put(
            Paths.operator_policies.detail(vhost=vhost, policy=policy), payload=value
        )

    def delete(self, vhost: str, policy: str) -> dict:
        """Delete an operator policy."""
        return self._http_client.delete(
            Paths.operator_policies.detail(vhost=vhost, policy=policy)
        )


class PoliciesAPI(BaseAPI):
    """
    Managing runtime policies and access to operator policy overrides.
    """

    def __init__(self, http_client: http_clients.HTTPClient) -> None:
        super().__init__(http_client)
        self.operator = OperatorPoliciesAPI(self._http_client)

    def all(self) -> list[dict]:
        """List all runtime policies in the cluster."""
        return self._http_client.get(Paths.policies.all())

    def by_vhost(self, vhost: str) -> list[dict]:
        """List all runtime policies in a specific virtual host."""
        return self._http_client.get(Paths.policies.by_vhost(vhost=vhost))

    def detail(self, vhost: str, policy: str) -> dict:
        """Get details of an individual runtime policy."""
        return self._http_client.get(Paths.policies.detail(vhost=vhost, policy=policy))

    def set(self, vhost: str, policy: str, value: dict) -> dict:
        """
        Create or update a runtime policy.

        Args:
            value: Dict with 'pattern' and 'definition' (mandatory),
                   plus 'priority' and 'apply-to' (optional).
        """
        return self._http_client.put(
            Paths.policies.detail(vhost=vhost, policy=policy), payload=value
        )

    def delete(self, vhost: str, policy: str) -> dict:
        """Delete a runtime policy."""
        return self._http_client.delete(
            Paths.policies.detail(vhost=vhost, policy=policy)
        )
