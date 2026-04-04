from typing import Union, get_args

from .const import BasePath, ProtocolUnit, TimeUnit


class Health:
    @staticmethod
    def alarms() -> str:
        return BasePath.HEALTH_ALARMS

    @staticmethod
    def certificate_expiration(*, within: int, unit: TimeUnit) -> str:
        if not isinstance(within, int) or within <= 0:
            raise ValueError("The 'within' argument must be a positive integer")

        valid_units = get_args(TimeUnit)
        if unit not in valid_units:
            raise ValueError(f"Invalid unit. Choose from: {', '.join(valid_units)}")

        return f"{BasePath.HEALTH_CERT}/{within}/{unit}"

    @staticmethod
    def local_alarms() -> str:
        return BasePath.HEALTH_LOCAL_ALARMS

    @staticmethod
    def mirror_critical() -> str:
        return BasePath.HEALTH_MIRROR_CRITICAL

    @staticmethod
    def port_listener(port: Union[int, str], /) -> str:
        if isinstance(port, str) and port.isdigit():
            port = int(port)

        if not isinstance(port, int) or not (1024 <= port <= 65535):
            raise ValueError(
                "Port must be an integer between 1024 and 65535 \
                (or a valid numeric string)"
            )

        return f"{BasePath.HEALTH_PORT}/{port}"

    @staticmethod
    def protocol_listener(protocol: ProtocolUnit) -> str:
        valid_protocols = get_args(ProtocolUnit)
        if protocol not in valid_protocols:
            raise ValueError(
                f"Invalid protocol. Choose from: {', '.join(valid_protocols)}"
            )

        return f"{BasePath.HEALTH_PROTOCOL}/{protocol}"

    @staticmethod
    def quorum_critical() -> str:
        return BasePath.HEALTH_QUORUM_CRITICAL

    @staticmethod
    def vhosts() -> str:
        return BasePath.HEALTH_VHOSTS
