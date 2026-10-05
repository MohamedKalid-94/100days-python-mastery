# Day 32 - Drawing Pad App
# Concept: Canvas Widgets
# Goal: Practice using the Canvas widget to draw shapes and respond to mouse movement

import tkinter as tk

window = tk.Tk()
window.title("Drawing Pad")
window.geometry("500x450")

# --- Creating a Canvas widget - a blank area for drawing ---
canvas = tk.Canvas(window, width=480, height=350, bg="white")
canvas.pack(pady=10)

# --- Drawing basic shapes on the canvas ---
# Coordinates are (x1, y1, x2, y2) - top-left and bottom-right corners
canvas.create_rectangle(20, 20, 100, 80, fill="lightblue", outline="blue")
canvas.create_oval(120, 20, 200, 80, fill="lightgreen", outline="green")
canvas.create_line(220, 20, 300, 80, fill="red", width=3)
canvas.create_text(350, 50, text="Canvas Shapes", font=("Arial", 12))

# --- current pen color, changeable via buttons below ---
current_color = "black"

# --- Free-hand drawing by tracking mouse movement ---
def draw(event):
    # event.x and event.y give the current mouse position on the canvas
    x, y = event.x, event.y
    radius = 3
    # drawing a tiny oval at each mouse position creates a "pen" effect
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=current_color, outline=current_color)

# --- <B1-Motion> fires whenever the mouse moves WHILE the left button is held down ---
canvas.bind("<B1-Motion>", draw)

# --- Tracking the last position to draw connected lines instead of dots ---
last_x, last_y = None, None

def draw_line(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y, fill=current_color, width=2)
    last_x, last_y = event.x, event.y

def reset_last_position(event):
    global last_x, last_y
    last_x, last_y = None, None

# --- Rebinding to the smoother line-drawing version instead ---
canvas.bind("<B1-Motion>", draw_line)
canvas.bind("<ButtonRelease-1>", reset_last_position)   # fires when the mouse button is released

# --- Buttons to change the pen color ---
def set_color(color):
    global current_color
    current_color = color

button_frame = tk.Frame(window)   # a Frame groups widgets together
button_frame.pack(pady=5)

colors = ["black", "red", "blue", "green", "orange"]
for color in colors:
    color_button = tk.Button(button_frame, bg=color, width=3, command=lambda c=color: set_color(c))
    color_button.pack(side="left", padx=2)
    # NOTE: lambda c=color captures the CURRENT color at loop time -
    # without it, every button would end up using the LAST color in the loop

# --- A button to clear the entire canvas ---
def clear_canvas():
    canvas.delete("all")   # removes everything drawn on the canvas

clear_button = tk.Button(window, text="Clear Canvas", command=clear_canvas)
clear_button.pack(pady=10)

window.mainloop()