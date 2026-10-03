# Day 31 - BMI Calculator
# Concept: Input Fields
# Goal: Practice taking multiple inputs from Entry widgets and validating them

import tkinter as tk

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("350x300")

# --- Weight input field ---
weight_label = tk.Label(window, text="Weight (kg):", font=("Arial", 12))
weight_label.pack(pady=(20, 0))

weight_entry = tk.Entry(window, width=20, font=("Arial", 12))
weight_entry.pack(pady=5)

# --- Height input field ---
height_label = tk.Label(window, text="Height (m):", font=("Arial", 12))
height_label.pack()

height_entry = tk.Entry(window, width=20, font=("Arial", 12))
height_entry.pack(pady=5)

# --- Label to show the result (starts empty) ---
result_label = tk.Label(window, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=15)

# --- Function to calculate BMI, with input validation ---
def calculate_bmi():
    weight_text = weight_entry.get()
    height_text = height_entry.get()

    # --- Validation: check both fields are filled ---
    if not weight_text or not height_text:
        result_label.config(text="Please fill in both fields.", fg="red")
        return

    # --- Validation: check the values are actually numbers ---
    try:
        weight = float(weight_text)
        height = float(height_text)
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")
        return

    # --- Validation: check for sensible positive values ---
    if weight <= 0 or height <= 0:
        result_label.config(text="Values must be greater than zero.", fg="red")
        return

    # --- Calculating BMI ---
    bmi = weight / (height ** 2)

    # --- Determining the category based on BMI ranges ---
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    result_label.config(text=f"BMI: {bmi:.2f} ({category})", fg="blue")


calculate_button = tk.Button(window, text="Calculate BMI", font=("Arial", 12), command=calculate_bmi)
calculate_button.pack(pady=10)

# --- A "Clear" button to reset the fields ---
def clear_fields():
    weight_entry.delete(0, tk.END)   # deletes from index 0 to the END of the text
    height_entry.delete(0, tk.END)
    result_label.config(text="")

clear_button = tk.Button(window, text="Clear", font=("Arial", 10), command=clear_fields)
clear_button.pack()

# --- Setting a default/placeholder value in an Entry ---
weight_entry.insert(0, "")   # inserting an empty string at position 0 (no-op, shown for reference)

# --- Allowing the Enter key to also trigger the calculation ---
# .bind() on an Entry widget lets you respond to key events on that SPECIFIC widget
def on_enter_pressed(event):
    calculate_bmi()

weight_entry.bind("<Return>", on_enter_pressed)
height_entry.bind("<Return>", on_enter_pressed)

# --- Setting initial keyboard focus to the first field ---
weight_entry.focus()

window.mainloop()