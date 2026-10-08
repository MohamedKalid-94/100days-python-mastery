# Day 34 - To-Do List GUI
# Concept: Advanced Widgets
# Goal: Practice Listbox, Scrollbar, Checkbutton, and Frame widgets together

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("To-Do List")
window.geometry("400x450")

# --- A Frame to group the input row together ---
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=25, font=("Arial", 12))
task_entry.pack(side="left", padx=5)   # side="left" places widgets next to each other, not stacked


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)   # adds the task to the END of the Listbox
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task first.")


add_button = tk.Button(input_frame, text="Add", command=add_task)
add_button.pack(side="left")

# --- A Frame to hold the Listbox + Scrollbar together ---
list_frame = tk.Frame(window)
list_frame.pack(pady=10, fill="both", expand=True)

# --- Scrollbar - needs to be linked to the Listbox it controls ---
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

# --- Listbox - shows a scrollable list of items, supports selection ---
task_listbox = tk.Listbox(list_frame, width=40, height=12, font=("Arial", 11), yscrollcommand=scrollbar.set)
task_listbox.pack(side="left", fill="both", expand=True)

# --- Linking the scrollbar back to the listbox (two-way connection) ---
scrollbar.config(command=task_listbox.yview)


def delete_task():
    selected = task_listbox.curselection()   # returns a tuple of selected indexes, e.g. (2,)
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")


delete_button = tk.Button(window, text="Delete Selected", command=delete_task)
delete_button.pack(pady=5)


def mark_complete():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task_text = task_listbox.get(index)
        if not task_text.startswith("✓ "):
            task_listbox.delete(index)
            task_listbox.insert(index, f"✓ {task_text}")
    else:
        messagebox.showwarning("No Selection", "Please select a task to mark complete.")


complete_button = tk.Button(window, text="Mark Complete", command=mark_complete)
complete_button.pack(pady=5)

# --- Checkbutton - a toggle-able checkbox, often paired with a BooleanVar ---
show_completed_only = tk.BooleanVar(value=False)


def toggle_view():
    # In a real app this would filter the listbox - here we just show the state
    state = "ON" if show_completed_only.get() else "OFF"
    print(f"Show completed only: {state}")


checkbox = tk.Checkbutton(window, text="Show completed only", variable=show_completed_only, command=toggle_view)
checkbox.pack(pady=10)


def clear_all():
    if messagebox.askyesno("Confirm", "Clear the entire list?"):
        task_listbox.delete(0, tk.END)   # deleting a RANGE from index 0 to END clears everything


clear_button = tk.Button(window, text="Clear All", command=clear_all)
clear_button.pack(pady=5)

# --- Allowing Enter key in the entry to also add the task ---
task_entry.bind("<Return>", lambda event: add_task())

window.mainloop()