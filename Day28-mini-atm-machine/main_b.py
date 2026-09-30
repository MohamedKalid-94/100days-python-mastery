# Day 28b - OOP Extras
# Concept: __repr__, Abstract Classes, Composition
# Goal: Cover a few important OOP concepts that didn't fit into the main
#       Day22-28 track, using the same Account/Bank theme for continuity

from abc import ABC, abstractmethod


# ============================================================
# Part 1: __repr__ vs __str__
# ============================================================
# __str__  -> human-readable, used by print() and str()
# __repr__ -> developer-focused, used by the console/debugger, and as a
#             fallback for print() if __str__ isn't defined
# Good practice: define BOTH. __repr__ should ideally look like code
# that could recreate the object.

class Card:
    def __init__(self, holder_name, card_number):
        self.holder_name = holder_name
        self.card_number = card_number

    def __str__(self):
        # human-friendly - safe to show to a user
        return f"Card holder: {self.holder_name}, ending in {self.card_number[-4:]}"

    def __repr__(self):
        # developer-friendly - shows exactly how to reconstruct this object
        return f"Card('{self.holder_name}', '{self.card_number}')"


card = Card("Kalid", "1234567890123456")

print("--- __str__ vs __repr__ ---")
print(str(card))    # calls __str__
print(repr(card))   # calls __repr__

# Without print(), just typing an object name in a console shows __repr__
card_list = [card]
print("\nA list of objects shows __repr__ for each item:")
print(card_list)


# ============================================================
# Part 2: Abstract classes - forcing subclasses to implement something
# ============================================================
# ABC (Abstract Base Class) lets you define a method that EVERY subclass
# MUST implement. You cannot create an object of an abstract class directly.

class PaymentMethod(ABC):

    def __init__(self, owner_name):
        self.owner_name = owner_name

    # --- @abstractmethod means: "every subclass MUST override this" ---
    @abstractmethod
    def pay(self, amount):
        pass

    # --- Abstract classes CAN still have normal, shared methods too ---
    def show_owner(self):
        print(f"Payment method owned by: {self.owner_name}")


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


# --- This would raise an error - you CANNOT instantiate an abstract class ---
try:
    generic_payment = PaymentMethod("Kalid")
except TypeError as error:
    print(f"\nCan't create PaymentMethod directly: {error}")

# --- But subclasses that implement pay() work fine ---
credit_payment = CreditCardPayment("Kalid")
upi_payment = UPIPayment("Asha")

credit_payment.show_owner()   # inherited normal method
credit_payment.pay(500)

upi_payment.show_owner()
upi_payment.pay(300)

# --- What happens if a subclass FORGETS to implement the abstract method ---
class BrokenPayment(PaymentMethod):
    pass   # forgot to implement pay()

try:
    broken = BrokenPayment("Test")
except TypeError as error:
    print(f"\nCan't create BrokenPayment - missing implementation: {error}")


# ============================================================
# Part 3: Composition ("has-a") vs Inheritance ("is-a")
# ============================================================
# Inheritance: "a SavingsAccount IS-A Account" (used in Day28)
# Composition: "an Account HAS-A Card" - one class CONTAINS another as
# an attribute, instead of inheriting from it. Often a better design
# choice than inheritance when the relationship isn't truly "is-a".

class Chip:
    def __init__(self, chip_id):
        self.chip_id = chip_id

    def verify(self):
        return f"Chip {self.chip_id} verified."


class DebitCard:
    def __init__(self, card_number, chip_id):
        self.card_number = card_number
        self.chip = Chip(chip_id)   # composition - DebitCard HAS-A Chip

    def use_at_terminal(self):
        # DebitCard doesn't need to know HOW chip verification works internally,
        # it just delegates that responsibility to the Chip object
        result = self.chip.verify()
        print(f"Using card ending in {self.card_number[-4:]}: {result}")


class BankCustomer:
    def __init__(self, name, card_number, chip_id):
        self.name = name
        self.debit_card = DebitCard(card_number, chip_id)   # composition again - HAS-A DebitCard

    def make_payment(self):
        print(f"{self.name} is making a payment...")
        self.debit_card.use_at_terminal()


print("\n--- Composition example ---")
customer = BankCustomer("Kalid", "9876123456781234", "CHIP001")
customer.make_payment()

# --- Why composition can be better than inheritance here ---
# A BankCustomer is NOT a type of DebitCard, and a DebitCard is NOT a type
# of Chip - they just USE each other. Forcing this into inheritance
# (e.g. "class BankCustomer(DebitCard)") would be a misleading, awkward
# design. Composition models the real-world relationship more accurately.

print("\nRule of thumb: use inheritance for true 'is-a' relationships")
print("(SavingsAccount IS-A Account). Use composition for 'has-a'")
print("relationships (BankCustomer HAS-A DebitCard).")