from typing import Optional

from . import utils
from .const import BasePath


class Policies:
    def __call__(self, *, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return self.list()
        else:
            return self.by_vhost(vhost)

    @staticmethod
    def list() -> str:
        return BasePath.POLICIES

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.POLICIES}/{vhost}"

    @staticmethod
    def detail(vhost: str, policy: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        policy = utils.prepare_name(policy, "Policy")

        return f"{BasePath.POLICIES}/{vhost}/{policy}"


class OperatorPolicies:
    def __call__(self, *, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return self.list()
        else:
            return self.by_vhost(vhost)

    @staticmethod
    def list() -> str:
        return BasePath.OPERATOR_POLICIES

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.OPERATOR_POLICIES}/{vhost}"

    @staticmethod
    def detail(vhost: str, policy: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        policy = utils.prepare_name(policy, "Policy")

        return f"{BasePath.OPERATOR_POLICIES}/{vhost}/{policy}"
