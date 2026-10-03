# Day 30 - Click Counter App
# Concept: Buttons & Events
# Goal: Practice handling button click events and updating widget state

import tkinter as tk

window = tk.Tk()
window.title("Click Counter")
window.geometry("300x250")

# --- A variable to keep track of the click count ---
# Regular Python variables work, but Tkinter also has special "Variable"
# types (IntVar, StringVar, etc.) that link directly to widgets - shown below.
click_count = 0

# --- Displaying the current count ---
count_label = tk.Label(window, text=f"Clicks: {click_count}", font=("Arial", 20))
count_label.pack(pady=20)

# --- The event handler function - runs every time the button is clicked ---
def increment_count():
    global click_count   # needed to modify a variable defined outside the function
    click_count += 1
    count_label.config(text=f"Clicks: {click_count}")

click_button = tk.Button(window, text="Click Me!", font=("Arial", 14), command=increment_count)
click_button.pack(pady=10)

# --- A second button to reset the counter ---
def reset_count():
    global click_count
    click_count = 0
    count_label.config(text=f"Clicks: {click_count}")

reset_button = tk.Button(window, text="Reset", font=("Arial", 12), command=reset_count)
reset_button.pack(pady=5)

# --- Using tk.IntVar() instead of a plain variable ---
# IntVar is a special Tkinter variable that widgets can watch/update automatically.
# Useful when multiple widgets need to stay in sync with the same value.
double_click_count = tk.IntVar(value=0)

double_label = tk.Label(window, textvariable=double_click_count, font=("Arial", 16))
# textvariable links the label's text DIRECTLY to the IntVar - no .config() needed!

def increment_double():
    double_click_count.set(double_click_count.get() + 2)   # .get() reads, .set() writes

double_button = tk.Button(window, text="Click for +2", command=increment_double)
double_button.pack(pady=10)
double_label.pack()

# --- Binding events directly (not just button clicks) ---
# .bind() lets you respond to other events too - key presses, mouse movement, etc.
def on_key_press(event):
    print(f"Key pressed: {event.char}")

window.bind("<Key>", on_key_press)   # fires whenever ANY key is pressed

# --- Binding a mouse click anywhere on the window (not just a button) ---
def on_window_click(event):
    print(f"Window clicked at position: ({event.x}, {event.y})")

window.bind("<Button-1>", on_window_click)   # <Button-1> = left mouse click

# --- Disabling a button after a certain condition ---
def check_limit():
    if click_count >= 5:
        click_button.config(state="disabled", text="Limit reached!")

# Hooking the limit check into the same click event
def increment_and_check():
    increment_count()
    check_limit()

click_button.config(command=increment_and_check)   # reassigning the command

window.mainloop()