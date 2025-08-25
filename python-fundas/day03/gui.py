

# # multi window - three windows using PySide

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QScrollArea,
    QFrame,
)
from PySide6.QtCore import Qt
from pymongo import MongoClient
import sys

client = MongoClient("mongodb://localhost:27017/")
db = client["ems"]
collection = db["employees"]


class DetailsWindow(QWidget):
    def __init__(self, emp):
        super().__init__()
        self.setWindowTitle(f"{emp['first_name']} {emp['last_name']} - Details")
        self.setGeometry(400, 200, 300, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"First Name: {emp['first_name']}"))
        layout.addWidget(QLabel(f"Last Name: {emp['last_name']}"))
        layout.addWidget(QLabel(f"Salary: {emp['salary']}"))

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)


class EmployeesWindow(QWidget):
    def __init__(self, home_window):
        super().__init__()
        self.home_window = home_window
        self.setWindowTitle("Employees List")
        self.setGeometry(350, 150, 300, 300)

        main_layout = QVBoxLayout()

        main_layout.addWidget(QLabel("Employees", alignment=Qt.AlignCenter))

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QFrame()
        scroll_layout = QVBoxLayout(scroll_content)

        for emp in collection.find():
            row = QHBoxLayout()
            row.addWidget(QLabel(emp["first_name"], minimumWidth=100))
            view_btn = QPushButton("View Details")
            view_btn.clicked.connect(lambda checked, e=emp: self.show_details(e))
            row.addWidget(view_btn)
            scroll_layout.addLayout(row)

        scroll.setWidget(scroll_content)
        main_layout.addWidget(scroll)

        thank_label = QLabel("Thank you.", alignment=Qt.AlignCenter)
        main_layout.addWidget(thank_label)

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close_window)
        main_layout.addWidget(close_btn)

        self.setLayout(main_layout)

    def show_details(self, emp):
        self.details_win = DetailsWindow(emp)
        self.details_win.show()

    def close_window(self):
        self.close()
        self.home_window.show()


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EMS - Home Page")
        self.setGeometry(300, 100, 400, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to EMS", alignment=Qt.AlignCenter))

        view_btn = QPushButton("View Employees")
        view_btn.clicked.connect(self.open_employees)
        layout.addWidget(view_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def open_employees(self):
        self.hide()
        self.emp_win = EmployeesWindow(self)
        self.emp_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = HomeWindow()
    home.show()
    sys.exit(app.exec())


# # # multi window - three windows

# # import tkinter as tk
# # from tkinter import ttk
# # from pymongo import MongoClient

# # client = MongoClient("mongodb://localhost:27017/")
# # db = client["ems"]
# # collection = db["employees"]

# # def show_details(emp):
# #     details_win = tk.Toplevel(root)
# #     details_win.title(f"{emp['first_name']} {emp['last_name']} - Details")
# #     details_win.geometry("300x200")

# #     tk.Label(details_win, text=f"First Name: {emp['first_name']}").pack(pady=5)
# #     tk.Label(details_win, text=f"Last Name: {emp['last_name']}").pack(pady=5)
# #     tk.Label(details_win, text=f"Salary: {emp['salary']}").pack(pady=5)

# #     tk.Button(details_win, text="Close", command=details_win.destroy).pack(pady=10)

# # def open_employees():
# #     root.withdraw()

# #     emp_win = tk.Toplevel(root)
# #     emp_win.title("Employees List")
# #     emp_win.geometry("300x250")

# #     tk.Label(emp_win, text="Employees", font=("Arial", 12, "bold")).pack(pady=5)

# #     frame = tk.Frame(emp_win)
# #     frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# #     for emp in collection.find():
# #         row = tk.Frame(frame)
# #         row.pack(fill=tk.X, pady=2)

# #         tk.Label(row, text=emp["first_name"], width=15, anchor="w").pack(side=tk.LEFT)
# #         tk.Button(row, text="View Details", command=lambda e=emp: show_details(e)).pack(side=tk.RIGHT)

# #     tk.Label(emp_win, text="Thank you.").pack(pady=5)

# #     def close_emp_win():
# #         emp_win.destroy()
# #         root.deiconify()

# #     tk.Button(emp_win, text="Close", command=close_emp_win).pack(pady=5)

# #     emp_win.protocol("WM_DELETE_WINDOW", close_emp_win)

# # root = tk.Tk()
# # root.title("EMS - Home Page")
# # root.geometry("400x200")

# # tk.Label(root, text="Welcome to EMS", font=("Arial", 12, "bold")).pack(pady=30)
# # tk.Button(root, text="View Employees", command=open_employees).pack(pady=10)

# # root.mainloop()

# # # # multi window - two windows

# # # import tkinter as tk
# # # from tkinter import ttk
# # # from pymongo import MongoClient

# # # client = MongoClient("mongodb://localhost:27017/")
# # # db = client["ems"]
# # # collection = db["employees"]


# # # def open_employees():
# # #     root.withdraw()

# # #     emp_win = tk.Toplevel(root)
# # #     emp_win.title("Employees List")
# # #     emp_win.geometry("400x300")

# # #     title_label = tk.Label(emp_win, text="Employee Data")
# # #     title_label.pack(pady=5)

# # #     tree = ttk.Treeview(
# # #         emp_win, columns=("First Name", "Last Name", "Salary"), show="headings"
# # #     )
# # #     tree.heading("First Name", text="First Name")
# # #     tree.heading("Last Name", text="Last Name")
# # #     tree.heading("Salary", text="Salary")
# # #     tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# # #     for emp in collection.find():
# # #         tree.insert(
# # #             "", tk.END, values=(emp["first_name"], emp["last_name"], emp["salary"])
# # #         )

# # #     footer_label = tk.Label(emp_win, text="Thank you.")
# # #     footer_label.pack(pady=5)

# # #     def close_emp_win():
# # #         emp_win.destroy()
# # #         root.deiconify()

# # #     done_btn = tk.Button(emp_win, text="Done", command=close_emp_win)
# # #     done_btn.pack(pady=5)

# # #     emp_win.protocol("WM_DELETE_WINDOW", close_emp_win)


# # # root = tk.Tk()
# # # root.title("EMS - Home Page")
# # # root.geometry("400x200")

# # # home_label = tk.Label(root, text="Welcome to EMS")

# # # home_label.pack(pady=30)

# # # view_btn = tk.Button(root, text="View Employees", command=open_employees)
# # # view_btn.pack(pady=10)

# # # root.mainloop()


# # # # # import tkinter as tk
# # # # # from tkinter import ttk
# # # # # from pymongo import MongoClient

# # # # # client = MongoClient("mongodb://localhost:27017/")
# # # # # db = client["ems"]
# # # # # collection = db["employees"]

# # # # # root = tk.Tk()
# # # # # root.title("Employee Data from MongoDB")
# # # # # root.geometry("400x300")

# # # # # title_label = tk.Label(root, text="Employee Data")
# # # # # title_label.pack(pady=5)

# # # # # tree = ttk.Treeview(
# # # # #     root, columns=("First Name", "Last Name", "Salary"), show="headings"
# # # # # )
# # # # # tree.heading("First Name", text="First Name")
# # # # # tree.heading("Last Name", text="Last Name")
# # # # # tree.heading("Salary", text="Salary")

# # # # # tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# # # # # for emp in collection.find():
# # # # #     tree.insert("", tk.END, values=(emp["first_name"], emp["last_name"], emp["salary"]))

# # # # # footer_label = tk.Label(root, text="Thank you.")
# # # # # footer_label.pack(pady=5)

# # # # # root.mainloop()
