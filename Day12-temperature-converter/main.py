# Day 12 - Temperature Converter
# Concept: Functions with Return Values
# Goal: Practice writing functions that return values, instead of just printing

# --- A function that converts Celsius to Fahrenheit and RETURNS the result ---
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# --- A function that converts Fahrenheit to Celsius ---
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# --- A function that converts Celsius to Kelvin ---
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# --- A function that converts Kelvin to Celsius ---
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

# --- Calling the functions and using their RETURN VALUES ---
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")

temp_f2 = 98.6
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f2}°F is {temp_c2:.2f}°C")

temp_c3 = 0
temp_k = celsius_to_kelvin(temp_c3)
print(f"{temp_c3}°C is {temp_k}K")

# --- A function CAN return a value that's used directly in another calculation ---
# Here we chain two conversions: Celsius -> Fahrenheit -> back to Celsius
original = 37
converted = celsius_to_fahrenheit(original)
back_to_original = fahrenheit_to_celsius(converted)
print(f"\n{original}°C -> {converted}°F -> back to {back_to_original}°C")

# --- A function returning MULTIPLE values at once (as a tuple) ---
def convert_all(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    return fahrenheit, kelvin  # returns a tuple of two values

f_result, k_result = convert_all(20)
print(f"\n20°C = {f_result}°F = {k_result}K")

# --- The difference between a function that PRINTS vs one that RETURNS ---
def print_only(celsius):
    print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
    # no return statement, so this function returns None

def return_only(celsius):
    return celsius_to_fahrenheit(celsius)
    # this function gives back a usable value

print_only(30)                      # just prints, can't reuse the result
result = return_only(30)            # result is stored and can be reused
print("Stored result from return_only:", result)


# ============================================================
# Interactive part: a simple temperature converter menu
# ============================================================
print("\n--- Temperature Converter ---")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("Choose an option (1-4): ")
value = float(input("Enter the temperature value: "))

if choice == "1":
    print(f"Result: {celsius_to_fahrenheit(value):.2f}°F")
elif choice == "2":
    print(f"Result: {fahrenheit_to_celsius(value):.2f}°C")
elif choice == "3":
    print(f"Result: {celsius_to_kelvin(value):.2f}K")
elif choice == "4":
    print(f"Result: {kelvin_to_celsius(value):.2f}°C")
else:
    print("Invalid choice.")


# ============================================================
# Part 2: A few more function concepts worth knowing
# ============================================================

# --- Default parameter values ---
# If no unit is given, it defaults to "F"
def convert_from_celsius(celsius, unit="F"):
    if unit == "F":
        return celsius_to_fahrenheit(celsius)
    elif unit == "K":
        return celsius_to_kelvin(celsius)
    else:
        return celsius

print("\nUsing a default parameter:", convert_from_celsius(25))          # uses default "F"
print("Overriding the default:", convert_from_celsius(25, unit="K"))     # explicitly "K"

# --- Keyword arguments - calling by parameter name, not just position ---
result = celsius_to_fahrenheit(celsius=100)
print("\nCalled with a keyword argument:", result)

# --- *args - accepting a variable number of positional arguments ---
def convert_many_to_fahrenheit(*temperatures):
    # temperatures is a tuple of however many values were passed in
    return [celsius_to_fahrenheit(temp) for temp in temperatures]

many_results = convert_many_to_fahrenheit(0, 10, 20, 30, 40)
print("\nConverted many values with *args:", many_results)

# --- **kwargs - accepting a variable number of keyword arguments ---
def show_temperatures(**readings):
    # readings is a dictionary of however many name=value pairs were passed in
    for location, temp in readings.items():
        print(f"{location}: {temp}°C")

print("\nUsing **kwargs:")
show_temperatures(Bengaluru=28, Delhi=35, Mumbai=31)

# --- Type hints - not enforced, but standard in real/professional code ---
def celsius_to_fahrenheit_typed(celsius: float) -> float:
    """Convert a Celsius value to Fahrenheit."""
    return (celsius * 9 / 5) + 32

print("\nType-hinted function result:", celsius_to_fahrenheit_typed(15))

# --- Docstrings - standard way to document a function ---
def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    Convert a temperature from Kelvin to Fahrenheit.

    Parameters:
        kelvin (float): temperature in Kelvin

    Returns:
        float: temperature in Fahrenheit
    """
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

print("\nDocstring example result:", kelvin_to_fahrenheit(300))
print("Reading the docstring:", kelvin_to_fahrenheit.__doc__)

# --- Early return pattern - return early on invalid input ---
def safe_celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return None  # exit early - physically impossible temperature
    return celsius_to_fahrenheit(celsius)

print("\nEarly return with invalid input:", safe_celsius_to_fahrenheit(-500))
print("Early return with valid input:", safe_celsius_to_fahrenheit(20))

# --- Lambda functions - short, throwaway one-line functions ---
celsius_to_fahrenheit_lambda = lambda c: (c * 9 / 5) + 32
print("\nLambda function result:", celsius_to_fahrenheit_lambda(25))