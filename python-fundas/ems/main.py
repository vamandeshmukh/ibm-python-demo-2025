# main.py

import sys

sys.path.append(".")


from model.Employee import Employee
from calc_stuff import add_nums


print("main")
sum = add_nums(10, 20)
print(sum)

emp = Employee(101, "Sonu", 10.50)
print(emp)
