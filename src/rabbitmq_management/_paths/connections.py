from typing import Optional

from . import utils
from .const import BasePath


class Connections:
    def __call__(self, *, connection: Optional[str] = None) -> str:
        if connection is None:
            return self.list()
        else:
            return self.detail(connection)

    @staticmethod
    def list() -> str:
        return BasePath.CONNECTIONS

    @staticmethod
    def detail(connection: str) -> str:
        connection = utils.prepare_connection(connection)
        return f"{BasePath.CONNECTIONS}/{connection}"

    @staticmethod
    def by_user(username: str) -> str:
        username = utils.prepare_username(username)
        return f"{BasePath.CONNECTIONS}/username/{username}"

    @staticmethod
    def channels(connection: str) -> str:
        connection = utils.prepare_connection(connection)
        return f"{BasePath.CONNECTIONS}/{connection}/channels"
