# Day 29 - Simple GUI App
# Concept: Tkinter Basics
# Goal: Practice creating a basic window and adding simple widgets

import tkinter as tk

# --- Creating the main application window ---
window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("400x300")   # width x height in pixels

# --- Adding a Label widget - displays text ---
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 16))
label.pack()   # .pack() places the widget in the window

# --- Adding a second label with different styling ---
subtitle = tk.Label(window, text="This is Day 29 of my Python journey.", font=("Arial", 10), fg="gray")
subtitle.pack(pady=10)   # pady adds vertical spacing around the widget

# --- Adding a Button widget ---
def on_button_click():
    label.config(text="Button was clicked!")   # .config() updates a widget's properties

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# --- Adding an Entry widget - a single-line text input box ---
entry_label = tk.Label(window, text="Enter your name:")
entry_label.pack()

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

# --- A function that reads from the Entry and updates the Label ---
def greet_user():
    name = entry.get()   # .get() retrieves the current text in the entry box
    if name:
        label.config(text=f"Hello, {name}!")
    else:
        label.config(text="Please enter a name.")

greet_button = tk.Button(window, text="Greet Me", command=greet_user)
greet_button.pack(pady=5)

# --- Widget layout: pack() vs other options (mentioned, not used here) ---
# pack()  - stacks widgets in order (top to bottom by default) - used throughout this file
# grid()  - places widgets in a row/column table layout
# place() - places widgets at exact x/y coordinates
# Only ONE layout manager should be used per container to avoid conflicts.

# --- The main event loop - keeps the window open and responsive ---
# This line MUST be the last thing in a Tkinter script - it "listens"
# for clicks, typing, etc. and keeps the window from closing immediately.
window.mainloop()