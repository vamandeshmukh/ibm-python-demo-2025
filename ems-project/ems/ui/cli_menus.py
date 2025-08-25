from ..services import EmployeeService
from ..utils.helpers import ask_nonempty, ask_float

def run_main_menu():
    while True:
        print("""
======= EMS =======
1. List Employees
2. Hire Employee
0. Exit
""")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            emps = EmployeeService.list_employees()
            if not emps:
                print("No employees yet.")
            else:
                for e in emps:
                    print(f"{e.id} | {e.first_name} {e.last_name} | Salary: {e.salary}")
        elif choice == "2":
            first = ask_nonempty("First name: ")
            last = ask_nonempty("Last name: ")
            salary = ask_float("Salary: ")
            emp = EmployeeService.hire(first, last, salary)
            print(f"Hired employee #{emp.id}: {emp.first_name} {emp.last_name}")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
