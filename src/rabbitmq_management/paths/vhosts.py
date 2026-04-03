from typing import Optional, get_args

from . import utils
from .const import BasePath, VHostLimitName


class VHosts:
    @staticmethod
    def all() -> str:
        return BasePath.VHOSTS

    @staticmethod
    def channels(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.VHOSTS}/{vhost}/channels"

    @staticmethod
    def connections(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.VHOSTS}/{vhost}/connections"

    @staticmethod
    def detail(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.VHOSTS}/{vhost}"

    @staticmethod
    def limits(*, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return BasePath.VHOST_LIMITS

        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.VHOST_LIMITS}/{vhost}"

    @staticmethod
    def permissions(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.VHOSTS}/{vhost}/permissions"

    @staticmethod
    def set_limits(vhost: str, limit: VHostLimitName) -> str:
        vhost = utils.prepare_vhost(vhost)
        valid_limit_names = get_args(VHostLimitName)
        if limit not in valid_limit_names:
            raise ValueError(f"Limit should be one of: {valid_limit_names}")

        return f"{BasePath.VHOST_LIMITS}/{vhost}/{limit}"

    @staticmethod
    def start(vhost: str, node: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        node = utils.prepare_node(node)

        return f"{BasePath.VHOSTS}/{vhost}/start/{node}"

    @staticmethod
    def topic_permissions(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.VHOSTS}/{vhost}/topic-permissions"
