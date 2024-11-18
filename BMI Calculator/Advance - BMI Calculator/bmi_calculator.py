# in your terminal istanll "pip install matplotlib pandas" this library without single or double cotation, if already installed then dont need to install again.

import tkinter as tk
from tkinter import messagebox
from data_storage import save_data, get_user_data
from visualization import plot_bmi_trend

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def on_calculate():
    name = entry_name.get()
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive.")
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        save_data(name, weight, height, bmi, category)
        
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def on_view_history():
    name = entry_name.get()
    user_data = get_user_data(name)
    if user_data.empty:
        messagebox.showinfo("No Data", "No records found for this user.")
    else:
        plot_bmi_trend(name)

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

# Name Input
tk.Label(root, text="Enter your name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

# Weight Input
tk.Label(root, text="Enter your weight (kg):").grid(row=1, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1)

# Height Input
tk.Label(root, text="Enter your height (m):").grid(row=2, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate BMI", command=on_calculate)
btn_calculate.grid(row=3, columnspan=2)

# View History Button
btn_history = tk.Button(root, text="View BMI History", command=on_view_history)
btn_history.grid(row=4, columnspan=2)

root.mainloop()

# to running this use following command in your terminal:- python bmi_calculator.py
