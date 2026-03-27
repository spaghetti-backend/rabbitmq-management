from typing import Optional

from . import utils
from .const import BasePath


class Bindings:
    def __call__(self, *, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return self.list()
        else:
            return self.by_vhost(vhost)

    @staticmethod
    def list() -> str:
        return BasePath.BINDINGS

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.BINDINGS}/{vhost}"

    @staticmethod
    def exchange_to_queue(
        vhost: str, exchange: str, queue: str, *, props: Optional[str] = None
    ) -> str:
        vhost = utils.prepare_vhost(vhost)
        exchange = utils.prepare_exchange(exchange)
        queue = utils.prepare_queue(queue)

        if props is not None:
            props = "/" + utils.prepare_name(props, "Binding properties key")
        else:
            props = ""

        return f"{BasePath.BINDINGS}/{vhost}/e/{exchange}/q/{queue}{props}"

    @staticmethod
    def exchange_to_exchange(
        vhost: str, source: str, destination: str, *, props: Optional[str] = None
    ) -> str:
        vhost = utils.prepare_vhost(vhost)
        source = utils.prepare_exchange(source)
        destination = utils.prepare_exchange(destination)

        if props is not None:
            props = "/" + utils.prepare_name(props, "Binding properties key")
        else:
            props = ""

        return f"{BasePath.BINDINGS}/{vhost}/e/{source}/e/{destination}{props}"
