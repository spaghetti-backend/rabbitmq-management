from . import utils
from .const import BasePath


class TopicPermissions:
    @staticmethod
    def all() -> str:
        return BasePath.TOPIC_PERMISSIONS

    @staticmethod
    def individual(vhost: str, username: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        username = utils.prepare_username(username)

        return f"{BasePath.TOPIC_PERMISSIONS}/{vhost}/{username}"


class Permissions:
    topic = TopicPermissions

    @staticmethod
    def all() -> str:
        return BasePath.PERMISSIONS

    @staticmethod
    def individual(vhost: str, username: str) -> str:
        vhost = utils.prepare_vhost(vhost)
        username = utils.prepare_username(username)

        return f"{BasePath.PERMISSIONS}/{vhost}/{username}"
