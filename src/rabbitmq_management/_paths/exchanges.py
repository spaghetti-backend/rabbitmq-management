from typing import Optional

from . import utils
from .const import BasePath


class Exchanges:
    def __call__(self, *, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return self.list()
        else:
            return self.by_vhost(vhost)

    @staticmethod
    def list() -> str:
        return BasePath.EXCHANGES

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.EXCHANGES}/{vhost}"

    @staticmethod
    def detail(vhost: str, exchange: str, *, if_unused: bool = False) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)
        only_unused = "?if-unused=true" if if_unused else ""

        return f"{BasePath.EXCHANGES}/{vhost}/{exchange}{only_unused}"

    @staticmethod
    def source_bindings(vhost: str, exchange: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)

        return f"{BasePath.EXCHANGES}/{vhost}/{exchange}/bindings/source"

    @staticmethod
    def destination_bindings(vhost: str, exchange: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)

        return f"{BasePath.EXCHANGES}/{vhost}/{exchange}/bindings/destination"

    @staticmethod
    def publish(vhost: str, exchange: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)

        return f"{BasePath.EXCHANGES}/{vhost}/{exchange}/publish"
