from . import utils
from .const import BasePath


class Definitions:
    @staticmethod
    def all() -> str:
        return BasePath.DEFINITIONS

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.DEFINITIONS}/{vhost}"
