import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    # get user inputs from entry fields
    weight = weight_entry.get()
    height = height_entry.get()
    # calculate the BMI
    bmi = (float(weight) / (float(height)/100)**2)

    # display the result in a message box
    if bmi < 18.5:
        result = f"Your BMI is {bmi:.1f}\nYou are underweight"
    elif bmi < 25:
        result = f"Your BMI is {bmi:.1f}\nYou are normal"
    elif bmi < 30:
        result = f"Your BMI is {bmi:.1f}\nYou are overweight"
    elif bmi < 35:
        result = f"Your BMI is {bmi:.1f}\nYou are obese"
    else:
        result = f"Your BMI is {bmi:.1f}\nYou are extremely obese"
    
    messagebox.showinfo("BMI Calculator", result)

# create the main window
root = tk.Tk()
root.title("BMI Calculator")

# create labels and entry fields for weight and height
weight_label = tk.Label(root, text="Weight (kg):")
weight_entry = tk.Entry(root)
height_label = tk.Label(root, text="Height (cm):")
height_entry = tk.Entry(root)

# create a button to calculate the BMI
calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi) 

# place the widgets on the window using grid layout

weight_label.grid(row=0, column=0)
weight_entry.grid(row=0, column=1)
height_label.grid(row=1, column=0)
height_entry.grid(row=1, column=1)
calculate_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
