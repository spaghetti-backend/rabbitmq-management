from typing import Optional, get_args

from . import utils
from .const import BasePath, LimitName


class Users:
    @staticmethod
    def all() -> str:
        return BasePath.USERS

    @staticmethod
    def bulk_delete() -> str:
        return f"{BasePath.USERS}/bulk-delete"

    @staticmethod
    def detail(username: str) -> str:
        username = utils.prepare_username(username)
        return f"{BasePath.USERS}/{username}"

    @staticmethod
    def limits(*, username: Optional[str] = None) -> str:
        if username is None:
            return BasePath.USER_LIMITS
        else:
            username = utils.prepare_username(username)
            return f"{BasePath.USER_LIMITS}/{username}"

    @staticmethod
    def permissions(username: str) -> str:
        username = utils.prepare_username(username)
        return f"{BasePath.USERS}/{username}/permissions"

    @staticmethod
    def set_limits(username: str, limit: LimitName) -> str:
        username = utils.prepare_username(username)
        valid_limit_names = get_args(LimitName)
        if limit not in valid_limit_names:
            raise ValueError(f"Limit should be one of: {valid_limit_names}")

        return f"{BasePath.USER_LIMITS}/{username}/{limit}"

    @staticmethod
    def without_permissions() -> str:
        return f"{BasePath.USERS}/without-permissions"
