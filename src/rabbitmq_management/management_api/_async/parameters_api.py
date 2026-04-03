from typing import Any

from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class AsyncParametersAPI(BaseAPI):
    async def all(self) -> list[dict]:
        """
        A list of all vhost-scoped parameters.
        """
        return await self._http_client.get(Paths.parameters.all())

    async def by_component(self, component: str) -> list[dict]:
        """
        A list of all vhost-scoped parameters for a given component.
        """
        return await self._http_client.get(Paths.parameters.by_component(component))

    async def component_by_vhost(self, component: str, vhost: str) -> list[dict]:
        """
        A list of all vhost-scoped parameters for a given component and virtual host.
        """
        return await self._http_client.get(
            Paths.parameters.by_vhost(component=component, vhost=vhost)
        )

    async def detail(self, component: str, vhost: str, parameter: str) -> dict:
        """
        An individual vhost-scoped parameter.
        """
        return await self._http_client.get(
            Paths.parameters.detail(
                component=component, vhost=vhost, parameter=parameter
            )
        )

    async def set(self, component: str, vhost: str, parameter: str, value: Any) -> dict:
        """
        To set a parameter, you will need a 'value' looking something like this:

        {
          "vhost": "/",
          "component":"federation",
          "name":"local_username",
          "value":"guest"
        }
        """
        payload = {"value": value}
        payload["component"] = component
        payload["vhost"] = vhost
        payload["name"] = parameter

        return await self._http_client.put(
            Paths.parameters.detail(
                component=component, vhost=vhost, parameter=parameter
            ),
            payload=payload,
        )

    async def delete(self, component: str, vhost: str, parameter: str) -> dict:
        """
        Delete the parameter.
        """
        return await self._http_client.delete(
            Paths.parameters.detail(
                component=component, vhost=vhost, parameter=parameter
            )
        )

    async def global_parameters(self) -> list[dict]:
        """
        A list of all global parameters.
        """
        return await self._http_client.get(Paths.parameters.global_parameters())

    async def global_parameter_detail(self, parameter: str) -> dict:
        """
        An individual global parameter.
        """
        return await self._http_client.get(
            Paths.parameters.global_parameters(parameter=parameter)
        )

    async def set_global_parameter(self, parameter: str, value: Any) -> dict:
        """
        To set a global parameter, you will need a 'value' looking something like this:

        {
          "name": "user_vhost_mapping",
          "value": {
            "guest": "/",
            "rabbit":"warren"
          }
        }
        """
        payload = {"value": value}
        payload["name"] = parameter

        return await self._http_client.put(
            Paths.parameters.global_parameters(parameter=parameter),
            payload=payload,
        )

    async def delete_global_parameter(self, parameter: str) -> dict:
        """
        Delete the global parameter.
        """
        return await self._http_client.delete(
            Paths.parameters.global_parameters(parameter=parameter)
        )
