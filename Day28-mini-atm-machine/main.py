# Day 28 - Mini ATM Machine
# Concept: Final OOP Project
# Goal: Bring together everything from Day22-27 - constructors, encapsulation,
#       inheritance, polymorphism, and static/class methods - in one project

class Account:

    # --- Class attribute - shared across all accounts ---
    bank_name = "Python National Bank"
    total_accounts = 0
    MIN_BALANCE = 100   # a constant-style class attribute

    def __init__(self, owner_name, pin, balance=0):
        self.owner_name = owner_name
        self.__pin = pin           # private - protected with encapsulation
        self.__balance = balance   # private - only accessible through methods/properties

        self.__transaction_history = []

        Account.total_accounts += 1
        self.account_number = f"ACC{Account.total_accounts:04d}"   # e.g. ACC0001

    # --- Property to safely READ the balance without exposing __balance directly ---
    @property
    def balance(self):
        return self.__balance

    # --- Private helper method - used internally only ---
    def __log_transaction(self, description):
        self.__transaction_history.append(description)

    # --- Public method with validation ---
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        self.__log_transaction(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.__balance - amount < Account.MIN_BALANCE:
            print(f"Cannot withdraw - minimum balance of {Account.MIN_BALANCE} must be maintained.")
        else:
            self.__balance -= amount
            self.__log_transaction(f"Withdrew {amount}")
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    # --- Verifying the PIN without ever exposing it ---
    def verify_pin(self, attempt):
        return self.__pin == attempt

    def show_history(self):
        print(f"\n--- Transaction history for {self.owner_name} ---")
        if not self.__transaction_history:
            print("No transactions yet.")
        for entry in self.__transaction_history:
            print(entry)

    # --- Class method - alternate constructor from a dictionary ---
    @classmethod
    def from_dict(cls, data):
        return cls(data["owner_name"], data["pin"], data.get("balance", 0))

    # --- Static method - a helper related to accounts, but not tied to one object ---
    @staticmethod
    def is_valid_pin(pin):
        return len(pin) == 4 and pin.isdigit()

    def __str__(self):
        return f"{self.account_number} - {self.owner_name} ({self.bank_name})"


# --- Inheritance: a SavingsAccount is a specialized Account ---
class SavingsAccount(Account):

    def __init__(self, owner_name, pin, balance=0, interest_rate=0.03):
        super().__init__(owner_name, pin, balance)
        self.interest_rate = interest_rate

    # --- A method that only SavingsAccount has ---
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest:.2f} added.")


# --- Another subclass, showing polymorphism through overriding ---
class CurrentAccount(Account):

    def __init__(self, owner_name, pin, balance=0, overdraft_limit=500):
        super().__init__(owner_name, pin, balance)
        self.overdraft_limit = overdraft_limit

    # --- Overriding withdraw() - current accounts allow overdraft ---
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance - amount < -self.overdraft_limit:
            print(f"Cannot withdraw - overdraft limit of {self.overdraft_limit} exceeded.")
        else:
            # accessing the private balance isn't possible directly here since it's
            # name-mangled to the PARENT class, so we go through the parent's own logic instead
            super().withdraw(amount) if self.balance >= amount else self._simulate_overdraft(amount)

    def _simulate_overdraft(self, amount):
        print(f"Overdraft used. Withdrew {amount} beyond available balance.")


# --- Creating different account types ---
account1 = SavingsAccount("Kalid", "1234", 1000)
account2 = CurrentAccount("Asha", "5678", 200, overdraft_limit=500)

print(account1)
print(account2)

# --- Using validation via static method BEFORE creating an account ---
new_pin = "12"
if Account.is_valid_pin(new_pin):
    print("\nValid PIN.")
else:
    print(f"\n'{new_pin}' is not a valid 4-digit PIN.")

# --- Depositing and withdrawing - polymorphism means each type behaves correctly ---
account1.deposit(500)
account1.add_interest()
account1.withdraw(50)

print()
account2.deposit(100)
account2.withdraw(700)   # uses overdraft since CurrentAccount overrides withdraw()

# --- PIN verification without ever exposing the real PIN ---
print("\n--- Login check ---")
print("Correct PIN:", account1.verify_pin("1234"))
print("Wrong PIN:", account1.verify_pin("0000"))

# --- Viewing transaction history ---
account1.show_history()

# --- Class-level info shared across all accounts ---
print(f"\nTotal accounts created: {Account.total_accounts}")

# --- Treating different account types the same way - polymorphism ---
all_accounts = [account1, account2]
print("\n--- All accounts summary ---")
for acc in all_accounts:
    print(f"{acc} - Balance: {acc.balance}")


# ============================================================
# Interactive ATM menu
# ============================================================
print("\n--- Mini ATM Machine ---")
current_account = account1   # simulate a logged-in user

while True:
    print(f"\nLogged in as: {current_account.owner_name}")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show transaction history")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Balance: {current_account.balance}")
    elif choice == "2":
        amount = float(input("Amount to deposit: "))
        current_account.deposit(amount)
    elif choice == "3":
        amount = float(input("Amount to withdraw: "))
        current_account.withdraw(amount)
    elif choice == "4":
        current_account.show_history()
    elif choice == "5":
        break
    else:
        print("Invalid option.")

print("\nThank you for using the Mini ATM. Goodbye!")