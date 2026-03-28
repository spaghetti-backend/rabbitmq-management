from . import utils
from .const import BasePath


class Channels:
    @staticmethod
    def all() -> str:
        return BasePath.CHANNELS

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.CHANNELS}/{vhost}"
