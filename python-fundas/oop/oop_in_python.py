# functions and methods 
# function - outside 
# method - inside class 

class Employee:
    
    # id: int
    # name: str 
    # salary: int

    # constructor method __init__
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    # def __str__(self):
    #     return self.name
    
    def get_salary(self):
        return self.salary

# instance methods, class methods, static methods 


    
emp = Employee(101, "Sonu", 20000)
# emp = Employee() # no constr 
print(emp)







