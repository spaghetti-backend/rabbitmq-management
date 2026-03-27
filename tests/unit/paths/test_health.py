from typing import Union

import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_certificate_expiration():
    assert (
        Paths.health.certificate_expiration(within=5, unit="days")
        == f"{BasePath.HEALTH_CERT}/5/days"
    )


@pytest.mark.parametrize("within", [None, 0])
def test_certificate_expiration_should_raise_error_when_incorrect_within_provided(
    within: int,
):
    with pytest.raises(ValueError, match="positive integer"):
        Paths.health.certificate_expiration(within=within, unit="years")


@pytest.mark.parametrize("unit", [None, "", "test"])
def test_certificate_expiration_should_raise_error_when_incorrect_unit_provided(unit):
    with pytest.raises(ValueError, match="Invalid unit"):
        Paths.health.certificate_expiration(within=1, unit=unit)


@pytest.mark.parametrize(
    "port, expected",
    [
        (5672, f"{BasePath.HEALTH_PORT}/5672"),
        ("61613", f"{BasePath.HEALTH_PORT}/61613"),
    ],
)
def test_port_listener(port: Union[str, int], expected: str):
    assert Paths.health.port_listener(port) == expected


@pytest.mark.parametrize("port", [None, 1023, 65536, "test"])
def test_port_listener_should_raise_error_when_incorrect_port_provided(port):
    with pytest.raises(ValueError):
        Paths.health.port_listener(port)


def test_protocol_listener():
    assert (
        Paths.health.protocol_listener("web-stomp")
        == f"{BasePath.HEALTH_PROTOCOL}/web-stomp"
    )


@pytest.mark.parametrize("protocol", [None, "", "test"])
def test_protocol_listener_should_raise_error_when_incorrect_protocol_provided(
    protocol,
):
    with pytest.raises(ValueError):
        Paths.health.protocol_listener(protocol)
