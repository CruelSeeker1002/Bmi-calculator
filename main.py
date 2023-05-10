import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI Calculator")
calc_method = tk.StringVar(value="metric")


weight_label = tk.Label(root, text="Weight:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()
height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()


def switch_units():
    global calc_method
    if calc_method.get() == "metric":
        calc_method.set("imperial")
        weight_label.config(text="Weight (lbs):")
        height_label.config(text="Height (in):")
    else:
        calc_method.set("metric")
        weight_label.config(text="Weight (kg):")
        height_label.config(text="Height (cm):")

unit_button = tk.Button(root, text="Switch Units", command=switch_units)
unit_button.pack(side="top")

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    if calc_method.get() == 'metric':
        bmi = weight / (height/100)**2
    else:
        bmi = (weight * 703) / height**2
    result_label.config(text="BMI: {:.1f}".format(bmi))


calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi) 

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()
result_label = tk.Label(root, text="BMI: ")
result_label.pack()

root.mainloop() 
