# Day 22 - Bank Account Simulator
# Concept: Classes & Objects
# Goal: Practice defining a class and creating objects from it

# --- Defining a class ---
# A class is a blueprint. It doesn't do anything by itself -
# it describes what an object of this type will have and can do.
class BankAccount:

    # --- __init__ is the constructor - runs automatically when an object is created ---
    # 'self' refers to the specific object being created
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name   # instance attribute
        self.balance = balance         # instance attribute

    # --- A method - a function that belongs to the class ---
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner_name}'s balance: {self.balance}")


# --- Creating objects (instances) from the class ---
account1 = BankAccount("Kalid", 1000)
account2 = BankAccount("Asha", 500)

print("Object 1 type:", type(account1))
print("Object 2 type:", type(account2))

# --- Accessing attributes ---
print("\nAccount 1 owner:", account1.owner_name)
print("Account 1 balance:", account1.balance)

# --- Calling methods on an object ---
account1.deposit(200)
account1.withdraw(150)
account1.show_balance()

print()
account2.deposit(1000)
account2.withdraw(2000)   # should show insufficient balance
account2.show_balance()

# --- Each object has its OWN separate data ---
print("\n--- Objects are independent ---")
print("Account 1 balance:", account1.balance)
print("Account 2 balance:", account2.balance)

# --- Modifying an attribute directly (possible, but methods are the proper way) ---
account1.owner_name = "Kalid Ahmed"
print("\nUpdated owner name:", account1.owner_name)


# ============================================================
# Interactive part: create and manage your own account
# ============================================================
print("\n--- Create a bank account ---")
name = input("Enter account owner name: ")
starting_balance = float(input("Enter starting balance: "))

my_account = BankAccount(name, starting_balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        my_account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        my_account.withdraw(amount)
    elif choice == "3":
        my_account.show_balance()
    elif choice == "4":
        break
    else:
        print("Invalid option.")

print("\nGoodbye!")