# # functions and methods 
# # function - outside 
# # method - inside class 

# class Person: 
#     def _init_(self):
#         pass

#     def speak(self):
#         print('speaking...')

# class Employee (Person):
    
#     # id: int
#     # name: str 
#     # salary: int

#     # constructor method __init__
#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary

#     # def __str__(self):
#     #     return self.name
    
#     def get_salary(self):
#         return self.salary

# # instance methods, class methods, static methods 

#     @classmethod
#     def get_data(cls):
#         pass

#     @classmethod
#     def get_more_data(cls):
#         pass

#     @staticmethod
#     def get_yet_more_data():
#         pass

# emp = Employee(101, "Sonu", 20000)
# # emp = Employee() # no constr 
# print(emp)
# emp2 = Employee(102, "Monu", 3000)
# Employee.get_data()

# emp.speak()

# # employee = {}

# # def employee_Service():
# #     pass  



class Person:

    # def __new__(cls):
    #     pass 

    def __init__(self):
        print("person constructor called")

class Employee (Person): 

    def __init__(self):
        super()
        print("employee constructor called")

# per = Person()
emp = Employee()




# methods with __ and _ 

