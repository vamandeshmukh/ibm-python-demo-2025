from typing import Optional, List
from bson import ObjectId
from ..models import Employee
from .connector import get_db

db = get_db()

class EmployeeDAO:
    collection = db["employees"]

    @staticmethod
    def create(first_name: str, last_name: str, salary: float) -> Employee:
        doc = {"first_name": first_name, "last_name": last_name, "salary": salary}
        result = EmployeeDAO.collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        return Employee(id=doc["_id"], first_name=first_name, last_name=last_name, salary=salary)

    @staticmethod
    def get_all() -> List[Employee]:
        employees = []
        for doc in EmployeeDAO.collection.find():
            employees.append(Employee(
                id=str(doc["_id"]),
                first_name=doc["first_name"],
                last_name=doc["last_name"],
                salary=doc["salary"]
            ))
        return employees
