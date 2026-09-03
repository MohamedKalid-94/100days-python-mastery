# A simple welcome message
print("Welcome to Day 1 of my Python journey!")

# print() can take multiple arguments, separated by commas
# By default, they are joined with a space
print("Today's focus:", "Print Statements")

# You can control the separator between arguments using sep=
print("Python", "Fundamentals", "100 Days", sep=" | ")

# You can control what's printed at the end using end=
# By default end="\n" (a new line). Here we override it.
print("Loading", end="")
print("...", end="")
print(" Done!")

# Printing an empty line for spacing
print()

# Multi-line message using triple quotes
print("""
========================================
   Welcome Message Generator - Day 01
========================================
""")

# A small "generator" - builds a message using a variable
name = "Kalid"
message = "Hello, " + name + "! Ready to build 100 projects?"
print(message)

# Same thing using an f-string (cleaner, more modern way)
print(f"Hello, {name}! Ready to build 100 projects?")