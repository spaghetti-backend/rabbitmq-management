from typing import Optional

import pytest

from rabbitmq_management._paths import BasePath, Paths


@pytest.mark.parametrize(
    "component, expected",
    [
        (None, BasePath.PARAMETERS),
        ("test\\component", f"{BasePath.PARAMETERS}/test%5Ccomponent"),
    ],
)
def test_parameters_endpoints(component: Optional[str], expected: str):
    assert Paths.parameters(component=component) == expected


def test_parameters_should_raise_error_when_component_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.parameters(component="")


def test_parameters_by_vhost_endpoint():
    assert (
        Paths.parameters.by_vhost("test\\component", "test\\vhost")
        == f"{BasePath.PARAMETERS}/test%5Ccomponent/test%5Cvhost"
    )


@pytest.mark.parametrize(
    "component, vhost",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_parameters_by_vhost_should_raise_error_when_name_is_empty(
    component: str, vhost: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.parameters.by_vhost(component, vhost)


def test_parameter_detail_endpoint():
    assert (
        Paths.parameters.detail("test\\component", "test\\vhost", "test\\parameter")
        == f"{BasePath.PARAMETERS}/test%5Ccomponent/test%5Cvhost/test%5Cparameter"
    )


@pytest.mark.parametrize(
    "component, vhost, parameter",
    [
        ("", "vhost", "parameter"),
        ("component", "", "parameter"),
        ("component", "vhost", ""),
    ],
)
def test_parameter_detail_should_raise_error_when_name_is_empty(
    component: str, vhost: str, parameter: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.parameters.detail(component, vhost, parameter)


@pytest.mark.parametrize(
    "parameter, expected",
    [
        (None, BasePath.GLOBAL_PARAMETERS),
        ("test\\parameter", f"{BasePath.GLOBAL_PARAMETERS}/test%5Cparameter"),
    ],
)
def test_global_parameters_endpoints(parameter: Optional[str], expected: str):
    assert Paths.parameters.global_parameters(parameter=parameter) == expected


def test_global_parameters_should_raise_error_when_component_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.parameters.global_parameters(parameter="")
