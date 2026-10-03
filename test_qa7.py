from uuid import uuid4

import pytest
import requests

from api.employee_api import EmployeeApi


@pytest.fixture
def employee_api():
    return EmployeeApi()


@pytest.fixture
def employee():
    suffix = uuid4().hex[:8]
    return {
        "first_name": "Dmitriy",
        "last_name": suffix,
        "email": f"dmitriy.{suffix}@example.com",
        "phone": "+49123456789",
        "is_active": True,
    }


@pytest.fixture
def employee_id(employee_api, employee):
    try:
        response = employee_api.create(employee)
    except requests.ConnectionError:
        pytest.skip("Employee API is unavailable")
    assert response.status_code in (200, 201)
    return response.json()["id"]


def test_create_employee(employee_api, employee):
    try:
        response = employee_api.create(employee)
    except requests.ConnectionError:
        pytest.skip("Employee API is unavailable")
    assert response.status_code in (200, 201)
    assert response.json()["id"]


def test_get_employee(employee_api, employee_id):
    response = employee_api.info(employee_id)
    assert response.status_code == 200
    assert response.json()["id"] == employee_id


def test_change_employee(employee_api, employee_id):
    response = employee_api.change(employee_id, {"first_name": "Dmitry"})
    assert response.status_code == 200
    assert employee_api.info(employee_id).json()["first_name"] == "Dmitry"
