# Day 11 - Safe Calculator
# Concept: Exception Handling
# Goal: Practice using try/except to handle errors gracefully instead of crashing

# --- Basic try/except ---
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"\n{num1} / {num2} = {result}")
except ZeroDivisionError:
    print("\nError: You cannot divide by zero.")
except ValueError:
    print("\nError: Please enter valid numbers only.")

# --- Catching multiple exception types in one line ---
try:
    value = int(input("\nEnter a whole number: "))
    print("You entered:", value)
except (ValueError, TypeError):
    print("Error: That wasn't a valid whole number.")

# --- Using else - runs ONLY if no exception occurred ---
try:
    number = int(input("\nEnter a number to check if it's even or odd: "))
except ValueError:
    print("Error: That's not a valid number.")
else:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# --- Using finally - runs NO MATTER WHAT (error or not) ---
try:
    amount = float(input("\nEnter an amount to withdraw: "))
    balance = 1000
    if amount > balance:
        raise ValueError("Insufficient balance")
    balance -= amount
    print(f"Withdrawal successful. New balance: {balance}")
except ValueError as error:
    print(f"Error: {error}")
finally:
    print("Transaction attempt finished (this always runs).")

# --- Raising your own exception with raise ---
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    user_age = int(input("\nEnter your age: "))
    check_age(user_age)
    print(f"Age accepted: {user_age}")
except ValueError as error:
    print(f"Error: {error}")


# ============================================================
# A full "safe calculator" that never crashes on bad input
# ============================================================
print("\n--- Safe Calculator ---")

while True:
    try:
        num1 = float(input("\nEnter the first number (or 'q' to quit): "))
    except ValueError:
        # allow quitting, otherwise show an error and try again
        break

    operator = input("Enter an operator (+, -, *, /): ")

    try:
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            raise ValueError("Invalid operator")

        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Calculation attempt complete.")

    again = input("\nCalculate again? (y/n): ")
    if again.lower() != "y":
        break

print("\nCalculator closed.")


# ============================================================
# Part 2: A few more exception handling concepts
# ============================================================

# --- Custom exception classes ---
# More professional than reusing ValueError for everything - gives
# your errors a specific, meaningful name.
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(f"Cannot withdraw {amount}, balance is only {balance}")
    return balance - amount


try:
    new_balance = withdraw(500, 800)
except InsufficientBalanceError as error:
    print(f"\nCustom exception caught: {error}")

# --- Common built-in exception types worth knowing by name ---
print("\n--- Common built-in exceptions (quick reference) ---")

try:
    result = "5" + 5  # mixing incompatible types
except TypeError as error:
    print(f"TypeError: {error}")

try:
    my_list = [1, 2, 3]
    print(my_list[10])  # index out of range
except IndexError as error:
    print(f"IndexError: {error}")

try:
    my_dict = {"a": 1}
    print(my_dict["b"])  # key doesn't exist
except KeyError as error:
    print(f"KeyError: {error}")

try:
    text = "hello"
    text.append("world")  # strings don't have .append()
except AttributeError as error:
    print(f"AttributeError: {error}")

try:
    with open("this_file_does_not_exist.txt", "r") as file:
        file.read()
except FileNotFoundError as error:
    print(f"FileNotFoundError: {error}")

# --- Nested try/except blocks ---
# A try block inside another try block, for handling errors at
# different levels - e.g. outer handles input errors,
# inner handles the calculation itself.
print("\n--- Nested try/except example ---")

try:
    user_input = input("Enter a number to divide 100 by: ")

    try:
        divisor = float(user_input)
        outcome = 100 / divisor
        print(f"100 / {divisor} = {outcome}")
    except ZeroDivisionError:
        print("Inner error: Cannot divide by zero.")

except ValueError:
    print("Outer error: That wasn't a valid number at all.")