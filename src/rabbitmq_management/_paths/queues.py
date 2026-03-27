from typing import Optional

from . import utils
from .const import BasePath


class Queues:
    def __call__(
        self,
        *,
        vhost: Optional[str] = None,
        enable_queue_totals: bool = False,
        disable_stats: bool = False,
    ) -> str:
        if vhost is None:
            return self.list(
                enable_queue_totals=enable_queue_totals,
                disable_stats=disable_stats,
            )
        else:
            return self.by_vhost(vhost)

    @staticmethod
    def list(*, enable_queue_totals: bool = False, disable_stats: bool = False) -> str:
        params = []
        if enable_queue_totals:
            params.append("enable_queue_totals=true")
        if disable_stats:
            params.append("disable_stats=true")

        if params:
            return f"{BasePath.QUEUES}?{'&'.join(params)}"
        else:
            return BasePath.QUEUES

    @staticmethod
    def by_vhost(vhost: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        return f"{BasePath.QUEUES}/{vhost}"

    @classmethod
    def detail(
        cls, vhost: str, queue: str, *, if_empty: bool = False, if_unused: bool = False
    ) -> str:
        path = cls._build_queue_path(vhost, queue, sub_path="")

        params = []
        if if_empty:
            params.append("if-empty=true")
        if if_unused:
            params.append("if-unused=true")

        if params:
            return f"{path}?{'&'.join(params)}"
        else:
            return path

    @classmethod
    def bindings(cls, vhost: str, queue: str) -> str:
        return cls._build_queue_path(vhost, queue, "bindings")

    @classmethod
    def contents(cls, vhost: str, queue: str) -> str:
        return cls._build_queue_path(vhost, queue, "contents")

    @classmethod
    def actions(cls, vhost: str, queue: str) -> str:
        return cls._build_queue_path(vhost, queue, "actions")

    @classmethod
    def messages(cls, vhost: str, queue: str) -> str:
        return cls._build_queue_path(vhost, queue, "get")

    @staticmethod
    def _build_queue_path(vhost: str, queue: str, sub_path: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        queue = utils.prepare_queue(queue)
        sub_path = f"/{sub_path}" if sub_path else ""
        return f"{BasePath.QUEUES}/{vhost}/{queue}{sub_path}"
