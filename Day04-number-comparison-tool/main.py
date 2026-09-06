# Day 04 - Number Comparison Tool
# Concept: If-Else Statements
# Goal: Compare numbers using conditional logic

# --- Take two numbers from the user ---
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# --- Basic if-elif-else comparison ---
print("\n--- Comparison ---")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

# --- Comparison operators return booleans directly ---
print("\n--- Raw boolean results ---")
print(f"{num1} > {num2}  -> {num1 > num2}")
print(f"{num1} < {num2}  -> {num1 < num2}")
print(f"{num1} == {num2} -> {num1 == num2}")
print(f"{num1} != {num2} -> {num1 != num2}")
print(f"{num1} >= {num2} -> {num1 >= num2}")
print(f"{num1} <= {num2} -> {num1 <= num2}")

# --- Nested if-else: check sign of a number ---
num3 = float(input("\nEnter a third number to check its sign: "))

if num3 > 0:
    if num3 % 2 == 0:
        print(f"{num3} is positive and even.")
    else:
        print(f"{num3} is positive and odd.")
elif num3 < 0:
    print(f"{num3} is negative.")
else:
    print(f"{num3} is zero.")

# --- Using logical operators (and / or) to combine conditions ---
print("\n--- Logical operators ---")
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
elif num1 < 0 or num2 < 0:
    print("At least one number is negative.")
else:
    print("At least one number is zero.")

# --- Finding the largest of the three numbers ---
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print(f"\nThe largest of the three numbers is: {largest}")