# Day 26 - Secure User Profile App
# Concept: Encapsulation
# Goal: Practice protecting an object's internal data using private attributes and properties

# --- Without encapsulation: anyone can set anything, even invalid values ---
class UnsafeUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password   # stored in plain sight, no protection at all

unsafe_user = UnsafeUser("kalid123", "mypassword")
unsafe_user.password = ""          # nothing stops this - a blank password is now allowed
print("Unsafe password after bad assignment:", repr(unsafe_user.password))


# --- With encapsulation: attributes are protected, access goes through controlled methods ---
class User:

    def __init__(self, username, password, age):
        self.username = username          # public - fine to access directly

        # --- Double underscore prefix = "private" attribute (name-mangled) ---
        # This signals "don't touch this directly from outside the class"
        self.__password = None
        self.__age = None

        # setting through the property setters below, so validation runs immediately
        self.password = password
        self.age = age

    # --- A property - lets you access a private attribute like a normal one ---
    # user.password  (looks like a plain attribute, but actually runs code)
    @property
    def password(self):
        return "********"   # never expose the real password, even internally on read

    # --- The setter - runs VALIDATION before allowing the value to be set ---
    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        self.__password = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120.")
        self.__age = value

    # --- A private helper method - only meant to be used INSIDE the class ---
    def __check_password(self, attempt):
        return self.__password == attempt

    # --- A public method that safely uses the private data/method internally ---
    def login(self, attempt):
        if self.__check_password(attempt):
            print(f"Welcome back, {self.username}!")
            return True
        else:
            print("Incorrect password.")
            return False

    def __str__(self):
        return f"User: {self.username}, Age: {self.age}"


# --- Creating a User the safe way ---
user = User("kalid123", "securepass", 30)
print("\n", user)

# --- Accessing through the property looks normal, but is protected ---
print("Displayed password:", user.password)   # always shows "********", never the real one

# --- Trying to set an invalid value gets REJECTED ---
try:
    user.password = "123"   # too short
except ValueError as error:
    print(f"\nRejected: {error}")

try:
    user.age = 200   # invalid age
except ValueError as error:
    print(f"Rejected: {error}")

# --- Logging in using the public method (which uses the private data safely) ---
print()
user.login("wrongpassword")
user.login("securepass")

# --- Directly accessing the "private" attribute from outside (discouraged, but possible) ---
# Python doesn't truly enforce privacy - the double underscore just "name-mangles" it.
# This is why it's called a CONVENTION, not a hard rule like in some other languages.
try:
    print(user.__password)
except AttributeError as error:
    print(f"\nCan't access directly: {error}")

# The real (mangled) name looks like this - shown here just to explain WHY it fails,
# not as something you should ever actually do in real code:
print("Mangled name still technically reachable:", user._User__password)


# ============================================================
# Interactive part: create your own secure profile
# ============================================================
print("\n--- Create your profile ---")
username = input("Username: ")

while True:
    try:
        new_password = input("Password (min 6 characters): ")
        new_age = int(input("Age: "))
        my_profile = User(username, new_password, new_age)
        break
    except ValueError as error:
        print(f"Invalid input: {error}. Try again.")

print("\nProfile created:", my_profile)

while True:
    attempt = input("\nEnter your password to log in (or 'quit'): ")
    if attempt == "quit":
        break
    my_profile.login(attempt)