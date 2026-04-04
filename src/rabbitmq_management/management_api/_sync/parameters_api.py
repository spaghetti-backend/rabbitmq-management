from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class ParametersAPI(BaseAPI):
    def all(self) -> list[dict]:
        """
        A list of all vhost-scoped parameters.
        """
        return self._http_client.get(Paths.parameters.all())

    def by_component(self, component: str) -> list[dict]:
        """
        A list of all vhost-scoped parameters for a given component.
        """
        return self._http_client.get(Paths.parameters.by_component(component))

    def component_by_vhost(self, component: str, vhost: str) -> list[dict]:
        """
        A list of all vhost-scoped parameters for a given component and virtual host.
        """
        return self._http_client.get(
            Paths.parameters.by_vhost(component=component, vhost=vhost)
        )

    def detail(self, component: str, vhost: str, parameter: str) -> dict:
        """
        An individual vhost-scoped parameter.
        """
        return self._http_client.get(
            Paths.parameters.detail(
                component=component, vhost=vhost, parameter=parameter
            )
        )

    def set(self, component: str, vhost: str, parameter: str, value: dict) -> dict:
        """
        To set a parameter, you will need a 'value' looking something like this:

        {
          "vhost": "/",
          "component":"federation",
          "name":"local_username",
          "value":"guest"
        }
        """
        payload = {
            "value": value,
            "component": component,
            "vhost": vhost,
            "name": parameter,
        }

        return self._http_client.put(
            Paths.parameters.detail(
                component=component, vhost=vhost, parameter=parameter
            ),
            payload=payload,
        )

    def delete(self, component: str, vhost: str, parameter: str) -> dict:
        """
        Delete the parameter.
        """
        return self._http_client.delete(
            Paths.parameters.detail(
                component=component, vhost=vhost, parameter=parameter
            )
        )

    def global_parameters(self) -> list[dict]:
        """
        A list of all global parameters.
        """
        return self._http_client.get(Paths.parameters.global_parameters())

    def global_parameter_detail(self, parameter: str) -> dict:
        """
        An individual global parameter.
        """
        return self._http_client.get(
            Paths.parameters.global_parameters(parameter=parameter)
        )

    def set_global_parameter(self, parameter: str, value: dict) -> dict:
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
        payload = {"value": value, "name": parameter}

        return self._http_client.put(
            Paths.parameters.global_parameters(parameter=parameter),
            payload=payload,
        )

    def delete_global_parameter(self, parameter: str) -> dict:
        """
        Delete the global parameter.
        """
        return self._http_client.delete(
            Paths.parameters.global_parameters(parameter=parameter)
        )
