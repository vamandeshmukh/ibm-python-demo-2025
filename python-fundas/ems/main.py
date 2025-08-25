# # main.py

# from model.Employee import Employee
# from calc_stuff import add_nums


# print("main")
# sum = add_nums(10, 20)
# print(sum)

# emp = Employee(101, "Sonu", 10.50)
# print(emp)


import tkinter as tk


def say_hello():
    label.config(text="Hello, Sonu!")


root = tk.Tk()
root.title("Tkinter Example")

label = tk.Label(root, text="Click the button")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=5)

root.mainloop()
