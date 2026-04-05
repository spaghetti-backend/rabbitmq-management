from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class ParametersAPI(BaseAPI):
    """
    Managing vhost-scoped and global RabbitMQ parameters (e.g., federation, shovels).
    """

    def all(self) -> list[dict]:
        """List all vhost-scoped parameters."""
        return self._http_client.get(Paths.parameters.all())

    def by_component(self, component: str) -> list[dict]:
        """List all vhost-scoped parameters for a specific component."""
        return self._http_client.get(Paths.parameters.by_component(component))

    def component_by_vhost(self, component: str, vhost: str) -> list[dict]:
        """List parameters for a specific component within a virtual host."""
        return self._http_client.get(
            Paths.parameters.by_vhost(component=component, vhost=vhost)
        )

    def detail(self, component: str, vhost: str, parameter: str) -> dict:
        """Get details of an individual vhost-scoped parameter."""
        return self._http_client.get(
            Paths.parameters.detail(
                component=component, vhost=vhost, parameter=parameter
            )
        )

    def set(self, component: str, vhost: str, parameter: str, value: dict) -> dict:
        """
        Create or update a vhost-scoped parameter.

        Args:
            value: The configuration value for the parameter.
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
        """Delete a vhost-scoped parameter."""
        return self._http_client.delete(
            Paths.parameters.detail(
                component=component, vhost=vhost, parameter=parameter
            )
        )

    def global_parameters(self) -> list[dict]:
        """List all global parameters."""
        return self._http_client.get(Paths.parameters.global_parameters())

    def global_parameter_detail(self, parameter: str) -> dict:
        """Get details of an individual global parameter."""
        return self._http_client.get(
            Paths.parameters.global_parameters(parameter=parameter)
        )

    def set_global_parameter(self, parameter: str, value: dict) -> dict:
        """
        Create or update a global parameter.

        Args:
            value: The configuration value for the global parameter.
        """
        payload = {"value": value, "name": parameter}

        return self._http_client.put(
            Paths.parameters.global_parameters(parameter=parameter),
            payload=payload,
        )

    def delete_global_parameter(self, parameter: str) -> dict:
        """Delete a global parameter."""
        return self._http_client.delete(
            Paths.parameters.global_parameters(parameter=parameter)
        )
