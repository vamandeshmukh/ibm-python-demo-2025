# from dataclasses import dataclass

# @dataclass

# class Employee:

#     id: int
#     name: str
#     salary: float

#     def print_data(self):
#         print(f"Employee {self.id}, {self.name}, {self.salary} ")

# emp1 = Employee(101, "Sonu", 10.50)
# emp2 = Employee(101, "Sonu", 10.50)
# print(emp1 == emp2)


# # # option 3 to create class


class Employee:

    id: int
    name: str
    salary: float

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name
            and self.salary == other.salary
        )

    def print_data(self):
        print(f"Employee {self.id}, {self.name}, {self.salary} ")


emp1 = Employee(101, "Sonu", 10.50)
emp2 = Employee(101, "Sonu", 10.50)
print(hash(emp1))
print(hash(emp2))
print(emp1 == emp2)

# @dataclass
# class Employee:

#     id: int
#     name: str
#     salary: float

#     def print_data(self):
#         print(f"Employee {self.id}, {self.name}, {self.salary} ")

# emp1 = Employee(101, "Sonu", 10.50)
# emp2 = Employee(101, "Sonu", 10.50)
# print(emp1 == emp2)

# # option 2 to create class

# class Employee:

#     def __init__(self):
#         pass

#     def print_data(self):
#         print(f"Employee {self.id}, {self.name}, {self.salary} ")


# emp = Employee()
# emp.print_data()

# option 1 to create class
# class Employee:

#     id: int
#     name: str
#     salary: float

#     def __init__(self):
#         pass

#     def print_data(self):
#         print(f"Employee {self.id}, {self.name}, {self.salary} ")


# emp = Employee()
# emp.print_data()


#     instance_field: int  # no initilization here
#     class_field = 11  # initilize here
#     # static_field

#     def instance_method(self):
#         print(f"instance_method {self}")

#     @classmethod
#     def class_method(cls):
#         print(f"class_method {cls}")

#     @staticmethod
#     def static_method():
#         print(f"static_method {Employee.class_field}")


# def some_function():
#     print(f"some_function {Employee.class_field}")


# emp = Employee()
# emp.instance_method()
# Employee.class_method()
# Employee.static_method()
# some_function()


# class Employee:

#     instance_field: int # no initilization here
#     class_field = 11 # initilize here
#     # static_field

#     def instance_method(self):
#         print(f"instance_method {self}")

#     @classmethod
#     def class_method(cls):
#         print(f"class_method {cls}")

#     @staticmethod
#     def static_method():
#         print(f"static_method {Employee.class_field}")


# def some_function():
#     print(f"some_function {Employee.class_field}")


# emp = Employee()
# emp.instance_method()
# Employee.class_method()
# Employee.static_method()
# some_function()
