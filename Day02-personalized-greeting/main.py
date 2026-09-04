# Day 02 - Personalized Greeting Program
# Concept: Variables & Data Types
# Goal: Practice creating variables of different types and using them in a greeting

# --- String variables ---
name = "Kalid"
city = "Bengaluru"

# --- Integer variable ---
age = 32

# --- Float variable ---
height_in_meters = 1.76

# --- Boolean variable ---
is_learning_python = True

# --- Checking the data type of a variable using type() ---
print("Data types:")
print(f"  name -> {type(name)}")
print(f"  age -> {type(age)}")
print(f"  height_in_meters -> {type(height_in_meters)}")
print(f"  is_learning_python -> {type(is_learning_python)}")
print()

# --- Using the variables to build a personalized greeting ---
print(f"Hello, {name}! Welcome to Day 2 of your Python journey.")
print(f"You are {age} years old and live in {city}.")
print(f"Your height is {height_in_meters} meters.")

# --- Using a boolean in a condition ---
if is_learning_python:
    print("You're currently learning Python. Keep going!")
else:
    print("Come back when you're ready to learn Python!")

print()

# --- Type casting: converting between data types ---
age_as_string = str(age)               # int -> str
height_as_int = int(height_in_meters)  # float -> int (truncates decimal)

print("Type casting examples:")
print(f"  age as string: '{age_as_string}' -> {type(age_as_string)}")
print(f"  height as int: {height_as_int} -> {type(height_as_int)}")

# --- Combining variables directly in a print statement ---
greeting = "Hi " + name + ", you are " + str(age) + " years old."
print(greeting)