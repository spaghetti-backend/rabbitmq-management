from . import utils
from .const import BasePath


class Connections:
    @staticmethod
    def all() -> str:
        return BasePath.CONNECTIONS

    @staticmethod
    def by_user(username: str) -> str:
        username = utils.prepare_username(username)
        return f"{BasePath.CONNECTIONS}/username/{username}"

    @staticmethod
    def channels(connection: str) -> str:
        connection = utils.prepare_connection(connection)
        return f"{BasePath.CONNECTIONS}/{connection}/channels"

    @staticmethod
    def detail(connection: str) -> str:
        connection = utils.prepare_connection(connection)
        return f"{BasePath.CONNECTIONS}/{connection}"
