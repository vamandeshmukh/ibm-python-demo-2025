import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ems"]
collection = db["employees"]

root = tk.Tk()
root.title("Employee Data from MongoDB")
root.geometry("400x300")

title_label = tk.Label(root, text="Employee Data")
title_label.pack(pady=5)

tree = ttk.Treeview(
    root, columns=("First Name", "Last Name", "Salary"), show="headings"
)
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Salary", text="Salary")

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

for emp in collection.find():
    tree.insert("", tk.END, values=(emp["first_name"], emp["last_name"], emp["salary"]))

footer_label = tk.Label(root, text="Thank you.")
footer_label.pack(pady=5)

root.mainloop()

