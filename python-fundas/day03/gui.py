# multi window - three windows 

import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ems"]
collection = db["employees"]

def show_details(emp):
    details_win = tk.Toplevel(root)
    details_win.title(f"{emp['first_name']} {emp['last_name']} - Details")
    details_win.geometry("300x200")

    tk.Label(details_win, text=f"First Name: {emp['first_name']}").pack(pady=5)
    tk.Label(details_win, text=f"Last Name: {emp['last_name']}").pack(pady=5)
    tk.Label(details_win, text=f"Salary: {emp['salary']}").pack(pady=5)

    tk.Button(details_win, text="Close", command=details_win.destroy).pack(pady=10)

def open_employees():
    root.withdraw()

    emp_win = tk.Toplevel(root)
    emp_win.title("Employees List")
    emp_win.geometry("300x250")

    tk.Label(emp_win, text="Employees", font=("Arial", 12, "bold")).pack(pady=5)

    frame = tk.Frame(emp_win)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    for emp in collection.find():
        row = tk.Frame(frame)
        row.pack(fill=tk.X, pady=2)

        tk.Label(row, text=emp["first_name"], width=15, anchor="w").pack(side=tk.LEFT)
        tk.Button(row, text="View Details", command=lambda e=emp: show_details(e)).pack(side=tk.RIGHT)

    tk.Label(emp_win, text="Thank you.").pack(pady=5)

    def close_emp_win():
        emp_win.destroy()
        root.deiconify()

    tk.Button(emp_win, text="Close", command=close_emp_win).pack(pady=5)

    emp_win.protocol("WM_DELETE_WINDOW", close_emp_win)

root = tk.Tk()
root.title("EMS - Home Page")
root.geometry("400x200")

tk.Label(root, text="Welcome to EMS", font=("Arial", 12, "bold")).pack(pady=30)
tk.Button(root, text="View Employees", command=open_employees).pack(pady=10)

root.mainloop()

# # multi window - two windows 

# import tkinter as tk
# from tkinter import ttk
# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client["ems"]
# collection = db["employees"]


# def open_employees():
#     root.withdraw()

#     emp_win = tk.Toplevel(root)
#     emp_win.title("Employees List")
#     emp_win.geometry("400x300")

#     title_label = tk.Label(emp_win, text="Employee Data")
#     title_label.pack(pady=5)

#     tree = ttk.Treeview(
#         emp_win, columns=("First Name", "Last Name", "Salary"), show="headings"
#     )
#     tree.heading("First Name", text="First Name")
#     tree.heading("Last Name", text="Last Name")
#     tree.heading("Salary", text="Salary")
#     tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

#     for emp in collection.find():
#         tree.insert(
#             "", tk.END, values=(emp["first_name"], emp["last_name"], emp["salary"])
#         )

#     footer_label = tk.Label(emp_win, text="Thank you.")
#     footer_label.pack(pady=5)

#     def close_emp_win():
#         emp_win.destroy()
#         root.deiconify()

#     done_btn = tk.Button(emp_win, text="Done", command=close_emp_win)
#     done_btn.pack(pady=5)

#     emp_win.protocol("WM_DELETE_WINDOW", close_emp_win)


# root = tk.Tk()
# root.title("EMS - Home Page")
# root.geometry("400x200")

# home_label = tk.Label(root, text="Welcome to EMS")

# home_label.pack(pady=30)

# view_btn = tk.Button(root, text="View Employees", command=open_employees)
# view_btn.pack(pady=10)

# root.mainloop()


# # # import tkinter as tk
# # # from tkinter import ttk
# # # from pymongo import MongoClient

# # # client = MongoClient("mongodb://localhost:27017/")
# # # db = client["ems"]
# # # collection = db["employees"]

# # # root = tk.Tk()
# # # root.title("Employee Data from MongoDB")
# # # root.geometry("400x300")

# # # title_label = tk.Label(root, text="Employee Data")
# # # title_label.pack(pady=5)

# # # tree = ttk.Treeview(
# # #     root, columns=("First Name", "Last Name", "Salary"), show="headings"
# # # )
# # # tree.heading("First Name", text="First Name")
# # # tree.heading("Last Name", text="Last Name")
# # # tree.heading("Salary", text="Salary")

# # # tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# # # for emp in collection.find():
# # #     tree.insert("", tk.END, values=(emp["first_name"], emp["last_name"], emp["salary"]))

# # # footer_label = tk.Label(root, text="Thank you.")
# # # footer_label.pack(pady=5)

# # # root.mainloop()
