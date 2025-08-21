# # # # functions and methods 
# # # # function - outside 
# # # # method - inside class 

# # # class Person: 
# # #     def _init_(self):
# # #         pass

# # #     def speak(self):
# # #         print('speaking...')

# # # class Employee (Person):
    
# # #     # id: int
# # #     # name: str 
# # #     # salary: int

# # #     # constructor method __init__
# # #     def __init__(self, id, name, salary):
# # #         self.id = id
# # #         self.name = name
# # #         self.salary = salary

# # #     # def __str__(self):
# # #     #     return self.name
    
# # #     def get_salary(self):
# # #         return self.salary

# # # # instance methods, class methods, static methods 

# # #     @classmethod
# # #     def get_data(cls):
# # #         pass

# # #     @classmethod
# # #     def get_more_data(cls):
# # #         pass

# # #     @staticmethod
# # #     def get_yet_more_data():
# # #         pass

# # # emp = Employee(101, "Sonu", 20000)
# # # # emp = Employee() # no constr 
# # # print(emp)
# # # emp2 = Employee(102, "Monu", 3000)
# # # Employee.get_data()

# # # emp.speak()

# # # # employee = {}

# # # # def employee_Service():
# # # #     pass  



# # class Person:

# #     # def __new__(cls):
# #     #     pass 

# #     def __init__(self):
# #         print("person constructor called")

# # class Employee (Person): 

# #     def __init__(self):
# #         print("employee constructor called")

# # # per = Person()
# # emp = Employee()

# # # methods with __ and _ 
# # # private protected public in Python 
# # # public = method /variable without any underescore 
# # # protected  = method /variable with single underescore 
# # # private  = method /variable with double underescore 
# # @property
# # @dataclass

# class Person: 

#     def __init__(self):
#         print("Person constructor")

#     def speak(self):
#         print('speaking...')

#     def _person_protected(self):
#         print("person protected method")

#     def __person_private(self):
#         print("person protected method")

# class Employee (Person):
    
#     def __init__(self):
#         super().__init__()
#         print("Employee constructor")

#     def __employee_private(self):
#         print("employee private method")

#     def _employee_protected(self):
#         print("employee protected method")

#     @property
#     def method_property(self):
#         print("method or property?")

# # per = Person()
# # per.speak()
# # # per.__person_private() # error 
# # per._person_protected() # works but don't call
# emp = Employee()
# # emp.speak()
# # # emp.__employee_private() # error 
# # # emp.__person_private() # error 
# # emp._employee_protected  # works but don't call
# # emp.method_property()
# emp.method_property

from  dataclasses import dataclass

@dataclass
class Employee:
    
    id: int
    name: str 
    salary: int

emp = Employee(101, "Sonu", 10.50)
print(emp)