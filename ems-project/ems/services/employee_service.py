from typing import List
from ..models import Employee
from ..database import EmployeeDAO

class EmployeeService:
    @staticmethod
    def hire(first_name: str, last_name: str, salary: float) -> Employee:
        return EmployeeDAO.create(first_name, last_name, salary)

    @staticmethod
    def list_employees() -> List[Employee]:
        return EmployeeDAO.get_all()
