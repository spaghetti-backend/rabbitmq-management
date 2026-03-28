from . import utils
from .const import BasePath


class Nodes:
    @staticmethod
    def all() -> str:
        return BasePath.NODES

    @staticmethod
    def detail(node: str, *, memory: bool = False, binary: bool = False) -> str:
        node = utils.prepare_node(node)
        path = f"{BasePath.NODES}/{node}"

        params = []
        if memory:
            params.append("memory=true")
        if binary:
            params.append("binary=true")

        if params:
            return f"{path}?{'&'.join(params)}"
        return path
