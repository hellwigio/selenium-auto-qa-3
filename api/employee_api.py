import requests


class EmployeeApi:
    BASE_URL = "http://5.101.50.27:8000/employee"

    def create(self, employee):
        return requests.post(f"{self.BASE_URL}/create", json=employee, timeout=10)

    def info(self, employee_id):
        return requests.get(f"{self.BASE_URL}/info", params={"id": employee_id}, timeout=10)

    def change(self, employee_id, employee):
        return requests.patch(
            f"{self.BASE_URL}/change",
            params={"id": employee_id},
            json=employee,
            timeout=10,
        )
