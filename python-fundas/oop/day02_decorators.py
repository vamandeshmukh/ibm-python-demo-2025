from abc import ABC, abstractmethod
from typing import final

# from typing import abstract


# class User:
# @final # not enforcing 
class User(ABC):

    @abstractmethod # enforcing 
    def login(self):
        print("user login")


class Rider(User):

    def login(self):
        print("Rider login")

    def logout(self):
        print("rider logout")


# user = User()
# user.login()
rider = Rider()
rider.login()
rider.logout()


# from dataclasses import *
# from typing import final

# # @dataclass
# # class Employee:

# #     id: int
# #     name: str
# #     __salary: float

# #     @property
# #     def get_salary(self):
# #         return self.__salary

# #     # @<property>.setter
# #     @__salary.setter
# #     def set_salary(self, salary):
# #         self.__salary = salary

# #     def print_data(self):
# #         print(f"Employee {self.id}, {self.name}, {self.salary} ")


# # emp1 = Employee(101, "Sonu", 10.50)
# # emp2 = Employee(101, "Sonu", 10.50)
# # print(emp1 == emp2)


# @final
# class ClassA:
#     id: int


# class ClassB(ClassA):
#     name: str


# obj = ClassB()
# print(obj)
