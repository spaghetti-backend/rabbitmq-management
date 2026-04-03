from rabbitmq_management.exceptions import RMQApiError
from rabbitmq_management.paths import Paths, TimeUnit
from rabbitmq_management.paths.const import ProtocolUnit

from .base_api import BaseAPI


class AsyncHealthAPI(BaseAPI):
    def alarms(self) -> dict:
        """
        Performs a health check for cluster alarms.

        Returns {"status": "ok"} when there are no alarms,
        and dictionary with the following structure if check failed:

        {
          "alarms": [
            {
              "node": "rabbit@rabbitmq",
              "resource": "memory"
              }
          ],
          "reason": "There are alarms in effect in the cluster",
          "status": "failed"
        }
        """
        try:
            return self._http_client.get(Paths.health.alarms())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            else:
                raise e

    def local_alarms(self) -> dict:
        """
        Performs a health check for alarms on the current node.

        Returns {"status": "ok"} when there are no alarms,
        and dictionary with the following structure if check failed:
        {
          "alarms": [
            {
              "node": "rabbit@rabbitmq",
              "resource": "memory"
              }
          ],
          "reason": "There are alarms in effect on the node",
          "status": "failed"
        }
        """
        try:
            return self._http_client.get(Paths.health.local_alarms())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            else:
                raise e

    def certificate_expiration(self, within: int, unit: TimeUnit) -> dict:
        """
        Checks the expiration date on the certificates for every listener configured to use TLS.

        Valid units: days, weeks, months, years.
        The value of the within argument is the number of units.
        So, when within is 2 and unit is "months",
        the expiration period used by the check will be the next two months.


        Returns {"status": "ok"} when there are no alarms,
        and dictionary with the following structure if check failed:
        {
          "status": "failed",
          "reason": "Certificates expiring",
          "expired": [
            {
              "cacertfile": "/etc/rabbitmq/certs/cert.pem",
              "cacertfile_expires_on": [
                "2026-04-01 19:31:01"
              ],
              "certfile": "/etc/rabbitmq/certs/cert.pem",
              "certfile_expires_on": [
                "2026-04-01 19:31:01"
              ],
              "interface": "::",
              "node": "rabbit@4d5eb24fab7b",
              "port": 5671,
              "protocol": "amqp/ssl"
            }
          ]
        }
        """
        try:
            return self._http_client.get(
                Paths.health.certificate_expiration(within=within, unit=unit)
            )
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            else:
                raise e

    def port_listener(self, port: int) -> dict:
        """
        Checks if there is an active listener on the give port

        Returns {"status": "ok", "port": 15672} when there are no alarms and 15672 port is given,
        and dictionary with the following structure if check failed:
        {
          "status": "failed",
          "reason": "No active listener",
          "missing": 15673,
          "ports": [
            15692,
            25672,
            5672,
            15672
          ]
        }
        """
        try:
            return self._http_client.get(Paths.health.port_listener(port))
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            else:
                raise e

    def protocol_listener(self, protocol: ProtocolUnit) -> dict:
        """
        Checks if there is an active listener for the given protocol.
        Valid protocol names are: amqp091, amqp10, mqtt, stomp, web-mqtt, web-stomp.

        Returns {"status": "ok", "protocol": "mqtt"} when there are no alarms and 'mqtt" protocol is given,
        and dictionary with the following structure if check failed:
        {
          "status": "failed",
          "reason": "No active listener",
          "missing": "mqtt",
          "protocols": [
            "http/prometheus",
            "clustering",
            "amqp",
            "http"
          ]
        }
        """
        try:
            return self._http_client.get(Paths.health.protocol_listener(protocol))
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            else:
                raise e

    def vhosts(self) -> dict:
        """
        Checks if all virtual hosts and running on the target node.
        """
        try:
            return self._http_client.get(Paths.health.vhosts())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            else:
                raise e

    def has_critical_mirror_sync(self) -> dict:
        """
        Checks if there are classic mirrored queues without synchronised mirrors online
        (queues that would potentially lose data if the target node is shut down).
        """
        try:
            return self._http_client.get(Paths.health.mirror_critical())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            else:
                raise e

    def node_quorum_critical(self) -> dict:
        """
        Checks if there are quorum queues with minimum online quorum
        (queues that would lose their quorum and availability if the target node is shut down).
        """
        try:
            return self._http_client.get(Paths.health.quorum_critical())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            else:
                raise e
