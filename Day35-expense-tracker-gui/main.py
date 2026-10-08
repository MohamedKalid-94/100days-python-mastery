# Day 35 - Expense Tracker App
# Concept: GUI Capstone
# Goal: Bring together everything from Day29-34 - widgets, layout, events,
#       message boxes, and Canvas/Listbox - into one complete GUI application

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Expense Tracker")
window.geometry("450x550")

# --- In-memory storage for expenses (a list of dicts, like we used in earlier days) ---
expenses = []

# ============================================================
# Top section: input form (Entry widgets + Frame layout)
# ============================================================
input_frame = tk.Frame(window)
input_frame.pack(pady=15)

tk.Label(input_frame, text="Description:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=5, pady=3)
description_entry = tk.Entry(input_frame, width=25)
description_entry.grid(row=0, column=1, padx=5, pady=3)

tk.Label(input_frame, text="Amount:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=5, pady=3)
amount_entry = tk.Entry(input_frame, width=25)
amount_entry.grid(row=1, column=1, padx=5, pady=3)

# --- Category dropdown using OptionMenu - a new widget for this capstone ---
tk.Label(input_frame, text="Category:", font=("Arial", 11)).grid(row=2, column=0, sticky="w", padx=5, pady=3)
category_var = tk.StringVar(value="Food")
categories = ["Food", "Transport", "Bills", "Entertainment", "Other"]
category_menu = tk.OptionMenu(input_frame, category_var, *categories)
category_menu.config(width=18)
category_menu.grid(row=2, column=1, padx=5, pady=3)

# --- grid() layout manager - used here instead of pack() for a form-like structure ---
# Note: grid() and pack() should not be mixed WITHIN the same container,
# but different containers (frames) can each use their own layout manager.


# ============================================================
# Functions - the app's logic, kept separate from widget setup
# ============================================================
def add_expense():
    description = description_entry.get()
    amount_text = amount_entry.get()
    category = category_var.get()

    if not description or not amount_text:
        messagebox.showwarning("Missing Info", "Please fill in both description and amount.")
        return

    try:
        amount = float(amount_text)
    except ValueError:
        messagebox.showerror("Invalid Amount", "Amount must be a number.")
        return

    if amount <= 0:
        messagebox.showerror("Invalid Amount", "Amount must be greater than zero.")
        return

    expense = {"description": description, "amount": amount, "category": category}
    expenses.append(expense)

    display_text = f"{description} - ₹{amount:.2f} ({category})"
    expense_listbox.insert(tk.END, display_text)

    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    update_total()


def delete_expense():
    selected = expense_listbox.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select an expense to delete.")
        return

    index = selected[0]
    expense_listbox.delete(index)
    del expenses[index]
    update_total()


def clear_all_expenses():
    if messagebox.askyesno("Confirm", "Clear all expenses?"):
        expense_listbox.delete(0, tk.END)
        expenses.clear()
        update_total()


def update_total():
    total = sum(expense["amount"] for expense in expenses)
    total_label.config(text=f"Total: ₹{total:.2f}")


def show_summary_by_category():
    if not expenses:
        messagebox.showinfo("Summary", "No expenses recorded yet.")
        return

    summary = {}
    for expense in expenses:
        cat = expense["category"]
        summary[cat] = summary.get(cat, 0) + expense["amount"]

    summary_text = "\n".join(f"{cat}: ₹{amount:.2f}" for cat, amount in summary.items())
    messagebox.showinfo("Spending by Category", summary_text)


add_button = tk.Button(window, text="Add Expense", command=add_expense)
add_button.pack(pady=5)


# ============================================================
# Middle section: Listbox with Scrollbar to show all expenses
# ============================================================
list_frame = tk.Frame(window)
list_frame.pack(pady=10, fill="both", expand=True, padx=15)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

expense_listbox = tk.Listbox(list_frame, height=10, yscrollcommand=scrollbar.set)
expense_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=expense_listbox.yview)


# ============================================================
# Bottom section: total, buttons
# ============================================================
total_label = tk.Label(window, text="Total: ₹0.00", font=("Arial", 14, "bold"))
total_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=5)

delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_expense)
delete_button.pack(side="left", padx=5)

summary_button = tk.Button(button_frame, text="Show Summary", command=show_summary_by_category)
summary_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all_expenses)
clear_button.pack(side="left", padx=5)

# --- Confirm before closing if there are unsaved expenses ---
def on_close():
    if expenses:
        if messagebox.askyesno("Exit", "You have unsaved expenses. Exit anyway?"):
            window.destroy()
    else:
        window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)

# --- Enter key support across the form ---
description_entry.bind("<Return>", lambda event: add_expense())
amount_entry.bind("<Return>", lambda event: add_expense())

window.mainloop()