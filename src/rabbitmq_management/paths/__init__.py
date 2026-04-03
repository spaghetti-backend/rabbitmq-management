from . import utils
from .auth import Auth
from .bindings import Bindings
from .channels import Channels
from .connections import Connections
from .const import BasePath, ProtocolUnit, TimeUnit, UserLimitName, VHostLimitName
from .consumers import Consumers
from .definitions import Definitions
from .exchanges import Exchanges
from .federation import Federation
from .health import Health
from .nodes import Nodes
from .parameters import Parameters
from .permissions import Permissions
from .policies import OperatorPolicies, Policies
from .queues import Queues
from .stream import Stream
from .users import Users
from .vhosts import VHosts


class Paths:
    auth = Auth
    bindings = Bindings
    channels = Channels
    connections = Connections
    consumers = Consumers
    definitions = Definitions
    exchanges = Exchanges
    federation = Federation
    health = Health
    nodes = Nodes
    parameters = Parameters
    permissions = Permissions
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
    def cluster_name() -> str:
        return BasePath.CLUSTER_NAME

    @staticmethod
    def extensions() -> str:
        return BasePath.EXTENSIONS

    @staticmethod
    def overview() -> str:
        return BasePath.OVERVIEW

    @staticmethod
    def rebalance_queues() -> str:
        return BasePath.REBALANCE_QUEUES

    @staticmethod
    def whoami() -> str:
        return BasePath.WHOAMI
