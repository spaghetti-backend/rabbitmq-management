from . import utils
from .const import BasePath


class Auth:
    @staticmethod
    def attempts(node: str) -> str:
        node = utils.prepare_node(node)
        return f"{BasePath.AUTH_ATTEMPTS}/{node}"

    @staticmethod
    def attempts_by_source(node: str) -> str:
        node = utils.prepare_node(node)

        return f"{BasePath.AUTH_ATTEMPTS}/{node}/source"

    @staticmethod
    def detail() -> str:
        return BasePath.AUTH

    @staticmethod
    def hash_password(password: str) -> str:
        password = utils.prepare_name(password, "Password")
        return f"{BasePath.AUTH_HASH_PASSWORD}/{password}"
