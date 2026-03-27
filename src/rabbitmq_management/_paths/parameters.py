from typing import Optional

from . import utils
from .const import BasePath


class Parameters:
    def __call__(self, *, component: Optional[str] = None) -> str:
        if component is None:
            return self.list()
        else:
            return self.by_component(component)

    @staticmethod
    def list() -> str:
        return BasePath.PARAMETERS

    @staticmethod
    def by_component(component: str) -> str:
        component = utils.prepare_component(component)
        return f"{BasePath.PARAMETERS}/{component}"

    @staticmethod
    def by_vhost(component: str, vhost: str) -> str:
        component = utils.prepare_component(component)
        vhost = utils.prepare_vhost(vhost)

        return f"{BasePath.PARAMETERS}/{component}/{vhost}"

    @staticmethod
    def detail(component: str, vhost: str, parameter: str) -> str:
        component = utils.prepare_component(component)
        vhost = utils.prepare_vhost(vhost)
        parameter = utils.prepare_parameter(parameter)

        return f"{BasePath.PARAMETERS}/{component}/{vhost}/{parameter}"

    @staticmethod
    def global_parameters(*, parameter: Optional[str] = None) -> str:
        if parameter is None:
            return BasePath.GLOBAL_PARAMETERS
        else:
            parameter = utils.prepare_parameter(parameter)
            return f"{BasePath.GLOBAL_PARAMETERS}/{parameter}"
