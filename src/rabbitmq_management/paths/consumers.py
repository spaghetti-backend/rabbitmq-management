from . import utils
from .const import BasePath


class Consumers:
    @staticmethod
    def all() -> str:
        return BasePath.CONSUMERS

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.CONSUMERS}/{vhost}"
