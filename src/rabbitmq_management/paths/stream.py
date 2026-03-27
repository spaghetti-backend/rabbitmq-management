from typing import Optional

from . import utils
from .const import BasePath


class Stream:
    @staticmethod
    def connections(*, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return BasePath.STREAM_CONNECTIONS
        else:
            vhost = utils.prepare_vhost(vhost)
            return f"{BasePath.STREAM_CONNECTIONS}/{vhost}"

    @staticmethod
    def connection_consumers(vhost: str, connection: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        connection = utils.prepare_connection(connection)
        return f"{BasePath.STREAM_CONNECTIONS}/{vhost}/{connection}/consumers"

    @staticmethod
    def connection_details(vhost: str, connection: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        connection = utils.prepare_connection(connection)
        return f"{BasePath.STREAM_CONNECTIONS}/{vhost}/{connection}"

    @staticmethod
    def connection_publishers(vhost: str, connection: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        connection = utils.prepare_connection(connection)
        return f"{BasePath.STREAM_CONNECTIONS}/{vhost}/{connection}/publishers"

    @staticmethod
    def consumers(*, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return BasePath.STREAM_CONSUMERS
        else:
            vhost = utils.prepare_vhost(vhost)
            return f"{BasePath.STREAM_CONSUMERS}/{vhost}"

    @staticmethod
    def publishers(*, vhost: Optional[str] = None) -> str:
        if vhost is None:
            return BasePath.STREAM_PUBLISHERS
        else:
            vhost = utils.prepare_vhost(vhost)
            return f"{BasePath.STREAM_PUBLISHERS}/{vhost}"

    @staticmethod
    def stream_publishers(vhost: str, stream: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        stream = utils.prepare_name(stream, "Stream")
        return f"{BasePath.STREAM_PUBLISHERS}/{vhost}/{stream}"
