from typing import Optional

from . import utils
from .auth import Auth
from .bindings import Bindings
from .connections import Connections
from .const import BasePath, LimitName, ProtocolUnit, TimeUnit
from .exchanges import Exchanges
from .health import Health
from .parameters import Parameters
from .policies import OperatorPolicies, Policies
from .queues import Queues
from .stream import Stream
from .users import Users
from .vhosts import VHosts


class Paths:
    auth = Auth
    bindings = Bindings
    connections = Connections
    exchanges = Exchanges
    health = Health
    parameters = Parameters
    policies = Policies
    operator_policies = OperatorPolicies
    queues = Queues
    stream = Stream
    users = Users
    vhosts = VHosts

    @staticmethod
    def aliveness_test(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.ALIVENESS_TEST}/{vhost}"

    @staticmethod
    def channels(*, channel: Optional[str] = None) -> str:
        if channel is None:
            return BasePath.CHANNELS

        channel = utils.prepare_channel(channel)
        return f"{BasePath.CHANNELS}/{channel}"

    @staticmethod
    def cluster_name() -> str:
        return BasePath.CLUSTER_NAME

    @staticmethod
    def consumers(*, consumer: Optional[str] = None) -> str:
        if consumer is None:
            return BasePath.CONSUMERS

        consumer = utils.prepare_consumer(consumer)
        return f"{BasePath.CONSUMERS}/{consumer}"

    @staticmethod
    def definitions(*, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return BasePath.DEFINITIONS

        vhost = utils.prepare_vhost(vhost)

        return f"{BasePath.DEFINITIONS}/{vhost}"

    @staticmethod
    def extensions() -> str:
        return BasePath.EXTENSIONS

    @staticmethod
    def federation_links(*, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return BasePath.FEDERATION_LINKS
        else:
            vhost = utils.prepare_vhost(vhost)
            return f"{BasePath.FEDERATION_LINKS}/{vhost}"

    @staticmethod
    def nodes(
        *, node: Optional[str] = None, memory: bool = False, binary: bool = False
    ) -> str:
        if node is None:
            return BasePath.NODES

        node = utils.prepare_node(node)
        path = f"{BasePath.NODES}/{node}"

        params = []
        if memory:
            params.append("memory=true")
        if binary:
            params.append("binary=true")

        if params:
            return f"{path}?{'&'.join(params)}"
        return path

    @staticmethod
    def overview() -> str:
        return BasePath.OVERVIEW

    @staticmethod
    def permissions(
        *, vhost: Optional[str] = None, username: Optional[str] = None
    ) -> str:
        if vhost is None and username is None:
            return BasePath.PERMISSIONS
        elif vhost is None or username is None:
            raise ValueError("Both vhost and username are required")
        else:
            vhost = utils.prepare_vhost(vhost)
            username = utils.prepare_username(username)

            return f"{BasePath.PERMISSIONS}/{vhost}/{username}"

    @staticmethod
    def rebalance_queues() -> str:
        return BasePath.REBALANCE_QUEUES

    @staticmethod
    def topic_permissions(
        *, vhost: Optional[str] = None, username: Optional[str] = None
    ) -> str:
        if vhost is None and username is None:
            return BasePath.TOPIC_PERMISSIONS
        elif vhost is None or username is None:
            raise ValueError("Both vhost and username are required")
        else:
            vhost = utils.prepare_vhost(vhost)
            username = utils.prepare_username(username)

            return f"{BasePath.TOPIC_PERMISSIONS}/{vhost}/{username}"

    @staticmethod
    def whoami() -> str:
        return BasePath.WHOAMI
