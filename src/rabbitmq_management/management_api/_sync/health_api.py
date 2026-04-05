from rabbitmq_management.exceptions import RMQApiError
from rabbitmq_management.paths import Paths
from rabbitmq_management.paths.const import ProtocolUnit, TimeUnit

from .base_api import BaseAPI


class AsyncHealthAPI(BaseAPI):
    """
    Health checks for monitoring RabbitMQ nodes and cluster status.
    """

    def alarms(self) -> dict:
        """
        Check for any active resource alarms in the cluster.

        Returns:
            {"status": "ok"} or a failure dict with alarm details.
        """
        try:
            return self._http_client.get(Paths.health.alarms())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            raise e

    def local_alarms(self) -> dict:
        """
        Check for active resource alarms on the target node.

        Returns:
            {"status": "ok"} or a failure dict with alarm details.
        """
        try:
            return self._http_client.get(Paths.health.local_alarms())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            raise e

    def certificate_expiration(self, within: int, unit: TimeUnit) -> dict:
        """
        Check for TLS certificates expiring within a given timeframe.

        Args:
            within: Number of time units.
            unit: Time unit (days, weeks, months, years).
        """
        try:
            return self._http_client.get(
                Paths.health.certificate_expiration(within=within, unit=unit)
            )
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            raise e

    def port_listener(self, port: int) -> dict:
        """
        Check if a specific port is actively listening.
        """
        try:
            return self._http_client.get(Paths.health.port_listener(port))
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            raise e

    def protocol_listener(self, protocol: ProtocolUnit) -> dict:
        """
        Check if an active listener exists for a specific protocol.

        Args:
            protocol: amqp091, amqp10, mqtt, stomp, web-mqtt, or web-stomp.
        """
        try:
            return self._http_client.get(Paths.health.protocol_listener(protocol))
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            raise e

    def vhosts(self) -> dict:
        """
        Check if all virtual hosts are running on the target node.
        """
        try:
            return self._http_client.get(Paths.health.vhosts())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            raise e

    def has_critical_mirror_sync(self) -> dict:
        """
        Check for classic mirrored queues at risk of data loss if node shuts down.
        """
        try:
            return self._http_client.get(Paths.health.mirror_critical())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            raise e

    def node_quorum_critical(self) -> dict:
        """
        Check for quorum queues at risk of losing availability if node shuts down.
        """
        try:
            return self._http_client.get(Paths.health.quorum_critical())
        except RMQApiError as e:
            if e.status_code == 503 and e.reason:
                return e.reason
            raise e
