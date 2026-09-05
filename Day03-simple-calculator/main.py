# Day 03 - Simple Calculator
# Concept: User Input & String Formatting
# Goal: Take input from the user, convert types, and format the output nicely

# --- input() always returns a string, so we convert it to a float ---
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# --- Basic arithmetic operations ---
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division needs a check to avoid dividing by zero
if num2 != 0:
    division = num1 / num2
else:
    division = None  # can't divide by zero

# --- String formatting: f-strings (recommended, modern way) ---
print("\n--- Results (f-string formatting) ---")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")

if division is not None:
    print(f"{num1} / {num2} = {division}")
else:
    print(f"{num1} / {num2} = undefined (cannot divide by zero)")

# --- Controlling decimal places using f-string format specifiers ---
# :.2f means "float, rounded to 2 decimal places"
print("\n--- Results (rounded to 2 decimal places) ---")
print(f"Addition:       {addition:.2f}")
print(f"Subtraction:    {subtraction:.2f}")
print(f"Multiplication: {multiplication:.2f}")

# --- Alternative formatting styles (good to know) ---
print("\n--- Same result using .format() method ---")
print("{} + {} = {}".format(num1, num2, addition))

print("\n--- Same result using % old-style formatting ---")
print("%.2f + %.2f = %.2f" % (num1, num2, addition))

# --- Bonus: using a simple operator chosen by the user ---
operator = input("\nPick an operator to see one result (+, -, *, /): ")

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Result: undefined (cannot divide by zero)")
else:
    print("Invalid operator entered.")