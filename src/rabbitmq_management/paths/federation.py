from . import utils
from .const import BasePath


class Federation:
    @staticmethod
    def links() -> str:
        return BasePath.FEDERATION_LINKS

    @staticmethod
    def links_by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.FEDERATION_LINKS}/{vhost}"
