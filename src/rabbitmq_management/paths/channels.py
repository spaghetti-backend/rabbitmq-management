from . import utils
from .const import BasePath


class Channels:
    @staticmethod
    def all() -> str:
        return BasePath.CHANNELS

    @staticmethod
    def detail(channel: str) -> str:
        channel = utils.prepare_channel(channel)
        return f"{BasePath.CHANNELS}/{channel}"
