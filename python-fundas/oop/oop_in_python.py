# # # functions and methods 
# # # function - outside 
# # # method - inside class 

# # class Person: 
# #     def _init_(self):
# #         pass

# #     def speak(self):
# #         print('speaking...')

# # class Employee (Person):
    
# #     # id: int
# #     # name: str 
# #     # salary: int

# #     # constructor method __init__
# #     def __init__(self, id, name, salary):
# #         self.id = id
# #         self.name = name
# #         self.salary = salary

# #     # def __str__(self):
# #     #     return self.name
    
# #     def get_salary(self):
# #         return self.salary

# # # instance methods, class methods, static methods 

# #     @classmethod
# #     def get_data(cls):
# #         pass

# #     @classmethod
# #     def get_more_data(cls):
# #         pass

# #     @staticmethod
# #     def get_yet_more_data():
# #         pass

# # emp = Employee(101, "Sonu", 20000)
# # # emp = Employee() # no constr 
# # print(emp)
# # emp2 = Employee(102, "Monu", 3000)
# # Employee.get_data()

# # emp.speak()

# # # employee = {}

# # # def employee_Service():
# # #     pass  



# class Person:

#     # def __new__(cls):
#     #     pass 

#     def __init__(self):
#         print("person constructor called")

# class Employee (Person): 

#     def __init__(self):
#         super()
#         print("employee constructor called")

# # per = Person()
# emp = Employee()

# # methods with __ and _ 
# # private protected public in Python 
# # public = method /variable without any underescore 
# # protected  = method /variable with single underescore 
# # private  = method /variable with double underescore 


class Person: 

    def _init_(self):
        print("Person constructor")

    def speak(self):
        print('speaking...')

    def _protected_method(self):
        print("protected method")

    def __private_method(self):
        print("protected method")

class Employee (Person):
    
    def __init__(self):
        print("Employee constructor")

    def __call_only_here(self):
        print("private method")

    def _call_only_in_subclass(self):
        print("protected method")


emp = Employee()

# emp.__call_only_here()
emp._call_only_in_subclass()
emp._protected_method()

per = Person()
# per.__private_method()
per._protected_method()
