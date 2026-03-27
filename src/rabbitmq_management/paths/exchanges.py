from . import utils
from .const import BasePath


class Exchanges:
    @staticmethod
    def all() -> str:
        return BasePath.EXCHANGES

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.EXCHANGES}/{vhost}"

    @staticmethod
    def destination_bindings(vhost: str, exchange: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)

        return f"{BasePath.EXCHANGES}/{vhost}/{exchange}/bindings/destination"

    @staticmethod
    def detail(vhost: str, exchange: str, *, if_unused: bool = False) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)
        only_unused = "?if-unused=true" if if_unused else ""

        return f"{BasePath.EXCHANGES}/{vhost}/{exchange}{only_unused}"

    @staticmethod
    def publish(vhost: str, exchange: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)

        return f"{BasePath.EXCHANGES}/{vhost}/{exchange}/publish"

    @staticmethod
    def source_bindings(vhost: str, exchange: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)

        return f"{BasePath.EXCHANGES}/{vhost}/{exchange}/bindings/source"
