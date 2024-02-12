import tkinter as tk
from tkinter import ttk

# Create a tkinter window
root = tk.Tk()

# Create a list of items for the dropdowns
savings_items = ["Savings Account 1", "Savings Account 2", "Savings Account 3"]
current_items = ["Current Account 1", "Current Account 2", "Current Account 3"]
rd_items = ["Recurring Deposit Account 1", "Recurring Deposit Account 2", "Recurring Deposit Account 3"]
fd_items = ["Fixed Deposit 1", "Fixed Deposit 2", "Fixed Deposit 3"]
salary_items = ["Salary Account 1", "Salary Account 2", "Salary Account 3"]

# Create the dropdown menus
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()

savings_dropdown = ttk.Combobox(root, textvariable=var1, values=savings_items)
current_dropdown = ttk.Combobox(root, textvariable=var2, values=current_items)
rd_dropdown = ttk.Combobox(root, textvariable=var3, values=rd_items)
fd_dropdown = ttk.Combobox(root, textvariable=var4, values=fd_items)
salary_dropdown = ttk.Combobox(root, textvariable=var5, values=salary_items)

# Set the dropdowns' positions on the grid
savings_dropdown.grid(row=0, column=0)
current_dropdown.grid(row=0, column=1)
rd_dropdown.grid(row=0, column=2)
fd_dropdown.grid(row=0, column=3)
salary_dropdown.grid(row=0, column=4)

# Set the default values for the dropdowns
savings_dropdown.current(0)
current_dropdown.current(0)
rd_dropdown.current(0)
fd_dropdown.current(0)
salary_dropdown.current(0)

# Run the tkinter event loop
root.mainloop()