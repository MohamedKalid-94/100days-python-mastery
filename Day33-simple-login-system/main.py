# Day 33 - Simple Login System
# Concept: Message Boxes
# Goal: Practice using tkinter's messagebox module for alerts, warnings, and confirmations

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Login System")
window.geometry("300x250")

# --- Hardcoded "database" of valid users for this demo ---
valid_users = {
    "kalid": "python123",
    "asha": "secure456",
}

# --- Username field ---
tk.Label(window, text="Username:", font=("Arial", 12)).pack(pady=(20, 0))
username_entry = tk.Entry(window, width=25)
username_entry.pack(pady=5)

# --- Password field - show="*" hides the typed characters ---
tk.Label(window, text="Password:", font=("Arial", 12)).pack()
password_entry = tk.Entry(window, width=25, show="*")
password_entry.pack(pady=5)


def attempt_login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        # --- messagebox.showwarning() - a warning icon, single OK button ---
        messagebox.showwarning("Missing Info", "Please enter both username and password.")
        return

    if username in valid_users and valid_users[username] == password:
        # --- messagebox.showinfo() - a plain info icon, single OK button ---
        messagebox.showinfo("Success", f"Welcome, {username}!")
    else:
        # --- messagebox.showerror() - an error icon, single OK button ---
        messagebox.showerror("Login Failed", "Incorrect username or password.")


login_button = tk.Button(window, text="Login", command=attempt_login)
login_button.pack(pady=10)


def clear_fields():
    # --- messagebox.askyesno() - asks a Yes/No question, returns True or False ---
    confirm = messagebox.askyesno("Confirm", "Clear the login fields?")
    if confirm:
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack()


def exit_app():
    # --- messagebox.askokcancel() - OK/Cancel style confirmation ---
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        window.destroy()   # closes the window/ends the program


exit_button = tk.Button(window, text="Exit", command=exit_app)
exit_button.pack(pady=10)

# --- Intercepting the window's own close ("X") button with a confirmation too ---
# .protocol() lets you override what happens on a specific window event
window.protocol("WM_DELETE_WINDOW", exit_app)

# --- messagebox.askretrycancel() and askyesnocancel() also exist ---
# askretrycancel() - Retry/Cancel, returns True/False
# askyesnocancel()  - Yes/No/Cancel, returns True/False/None
# Not demonstrated directly here, but worth knowing they exist for
# situations like "connection failed, retry?" or three-way choices.

window.mainloop()