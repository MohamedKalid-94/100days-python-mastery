# Day 27 - Inventory Management System
# Concept: Static & Class Methods
# Goal: Practice the difference between instance methods, class methods, and static methods

class Product:

    # --- Class attribute - shared across ALL Product objects ---
    total_products = 0
    tax_rate = 0.18   # 18% tax, same for every product

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        # every time a new Product is created, increase the shared counter
        Product.total_products += 1

    # --- A regular INSTANCE method - needs 'self', works with ONE specific object ---
    def get_total_value(self):
        return self.price * self.quantity

    def restock(self, amount):
        self.quantity += amount
        print(f"Restocked {self.name}. New quantity: {self.quantity}")

    # --- A CLASS method - works with the CLASS itself, not one object ---
    # Takes 'cls' instead of 'self'. Used when you need to access/modify
    # something shared across ALL objects, like the running total count.
    @classmethod
    def get_total_products(cls):
        return cls.total_products

    # --- A class method used as an ALTERNATE CONSTRUCTOR ---
    # A common real-world pattern: creating an object from a different
    # input format, e.g. a comma-separated string like "Pen,10,50"
    @classmethod
    def from_string(cls, data_string):
        name, price, quantity = data_string.split(",")
        return cls(name, float(price), int(quantity))   # cls(...) creates a new Product

    # --- A STATIC method - doesn't need 'self' OR 'cls' ---
    # It's just a regular function that logically belongs with the class,
    # because it's related to Products, even though it doesn't touch any
    # specific object's or the class's data.
    @staticmethod
    def calculate_price_with_tax(price):
        return price * (1 + Product.tax_rate)

    @staticmethod
    def is_valid_quantity(quantity):
        return quantity >= 0

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ {self.price} each"


# --- Creating products the normal way ---
product1 = Product("Pen", 10, 100)
product2 = Product("Notebook", 50, 30)

print(product1)
print(product2)

# --- Calling an INSTANCE method - needs a specific object ---
print(f"\nTotal value of {product1.name}: {product1.get_total_value()}")
product1.restock(20)

# --- Calling a CLASS method - can be called on the class itself, no object needed ---
print(f"\nTotal products created: {Product.get_total_products()}")

# --- It can also be called on an instance, but it still refers to the CLASS data ---
print("Same result via an instance:", product1.get_total_products())

# --- Using the alternate constructor (class method) ---
product3 = Product.from_string("Eraser,5,200")
print("\nCreated from string:", product3)
print("Total products now:", Product.get_total_products())

# --- Calling a STATIC method - doesn't need an object OR the class's data ---
price_with_tax = Product.calculate_price_with_tax(100)
print(f"\nPrice with tax on 100: {price_with_tax}")

# --- Static methods can also be called through an instance (less common, but works) ---
print("Same static call via instance:", product1.calculate_price_with_tax(100))

# --- Using a static method for simple validation, unrelated to any specific object ---
print("\nIs -5 a valid quantity?", Product.is_valid_quantity(-5))
print("Is 50 a valid quantity?", Product.is_valid_quantity(50))

# --- Summary of the three method types ---
print("\n--- Quick reference ---")
print("Instance method (self):  needs an object,     works on THAT object's data")
print("Class method (cls):      needs the class,      works on SHARED class data")
print("Static method:           needs neither,         just a related helper function")


# ============================================================
# Interactive part: manage an inventory
# ============================================================
inventory = [product1, product2, product3]

print("\n--- Inventory Management System ---")
while True:
    print("\n1. Show all products")
    print("2. Add product from string (name,price,quantity)")
    print("3. Restock a product")
    print("4. Show total products created")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        for p in inventory:
            print(p)
    elif choice == "2":
        data = input("Enter as name,price,quantity: ")
        new_product = Product.from_string(data)
        inventory.append(new_product)
        print("Added:", new_product)
    elif choice == "3":
        name = input("Product name to restock: ")
        amount = int(input("Amount to add: "))
        for p in inventory:
            if p.name.lower() == name.lower():
                p.restock(amount)
                break
        else:
            print("Product not found.")
    elif choice == "4":
        print("Total products ever created:", Product.get_total_products())
    elif choice == "5":
        break
    else:
        print("Invalid option.")

print("\nGoodbye!")