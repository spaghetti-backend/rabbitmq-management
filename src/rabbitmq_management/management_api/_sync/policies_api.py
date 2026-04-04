from rabbitmq_management import http_clients
from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class OperatorPoliciesAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of all operator policy overrides.
        """
        return self._http_client.get(Paths.operator_policies.all())

    def by_vhost(self, vhost: str) -> list[dict]:
        """
        A list of all operator policy overrides in a given virtual host.
        """
        return self._http_client.get(Paths.operator_policies.by_vhost(vhost=vhost))

    def detail(self, vhost: str, policy: str) -> dict:
        """
        An individual operator policy.
        """
        return self._http_client.get(
            Paths.operator_policies.detail(vhost=vhost, policy=policy)
        )

    def set(self, vhost: str, policy: str, value: dict) -> dict:
        """
        To set an operator policy, you will need a body looking something like this:

        {
          "pattern": "^amq.",
          "definition": {
            "expires": 100
          },
          "priority": 0,
          "apply-to": "queues"
        }

        'pattern' and 'definition' are mandatory,
        'priority' and 'apply-to' are optional.
        """
        return self._http_client.put(
            Paths.operator_policies.detail(vhost=vhost, policy=policy), payload=value
        )

    def delete(self, vhost: str, policy: str) -> dict:
        """
        Delete the operator policy.
        """
        return self._http_client.delete(
            Paths.operator_policies.detail(vhost=vhost, policy=policy)
        )


class PoliciesAPI(BaseAPI):
    def __init__(self, http_client: http_clients.HTTPClient) -> None:
        super().__init__(http_client)
        self.operator = OperatorPoliciesAPI(self._http_client)

    def all(self) -> list[dict]:
        """
        A list of all policies.
        """
        return self._http_client.get(Paths.policies.all())

    def by_vhost(self, vhost: str) -> list[dict]:
        """
        A list of all policies in a given virtual host.
        """
        return self._http_client.get(Paths.policies.by_vhost(vhost=vhost))

    def detail(self, vhost: str, policy: str) -> dict:
        """
        An individual policy.
        """
        return self._http_client.get(Paths.policies.detail(vhost=vhost, policy=policy))

    def set(self, vhost: str, policy: str, value: dict) -> dict:
        """
        To set a policy, you will need a body looking something like this:

        {
          "pattern": "^amq.",
          "definition": {
            "federation-upstream-set": "all"
          },
          "priority": 0,
          "apply-to": "all"
        }

        'pattern' and 'definition' are mandatory,
        'priority' and 'apply-to' are optional.
        """
        return self._http_client.put(
            Paths.policies.detail(vhost=vhost, policy=policy), payload=value
        )

    def delete(self, vhost: str, policy: str) -> dict:
        """
        Delete the policy.
        """
        return self._http_client.delete(
            Paths.policies.detail(vhost=vhost, policy=policy)
        )
