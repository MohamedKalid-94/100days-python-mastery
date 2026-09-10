# Day 08 - Contact Book
# Concept: Dictionaries
# Goal: Practice creating, updating, and working with Python dictionaries

# --- Creating an empty dictionary ---
contacts = {}

# --- Adding entries: key = name, value = phone number ---
contacts["Kalid"] = "9876543210"
contacts["Asha"] = "9123456780"
contacts["Ravi"] = "9988776655"
print("Contact book:", contacts)

# --- Accessing a value by key ---
print("\nKalid's number:", contacts["Kalid"])

# --- Using .get() to safely access a key that might not exist ---
number = contacts.get("Priya", "Not found")
print("Priya's number:", number)

# --- Updating an existing entry ---
contacts["Ravi"] = "9111222333"
print("\nAfter updating Ravi's number:", contacts)

# --- Checking if a key exists using 'in' ---
name_to_check = "Asha"
if name_to_check in contacts:
    print(f"\n{name_to_check} is in the contact book.")
else:
    print(f"\n{name_to_check} is NOT in the contact book.")

# --- Removing an entry with del ---
del contacts["Ravi"]
print("\nAfter deleting Ravi:", contacts)

# --- Removing an entry with .pop() (also returns the removed value) ---
removed_number = contacts.pop("Asha")
print(f"Removed Asha's number: {removed_number}")
print("Contact book now:", contacts)

# --- Looping through keys, values, and both ---
contacts["Kalid"] = "9876543210"
contacts["Meera"] = "9090909090"

print("\n--- Names only (.keys()) ---")
for name in contacts.keys():
    print(name)

print("\n--- Numbers only (.values()) ---")
for number in contacts.values():
    print(number)

print("\n--- Name and number together (.items()) ---")
for name, number in contacts.items():
    print(f"{name}: {number}")

# --- Number of entries using len() ---
print(f"\nTotal contacts: {len(contacts)}")


# ============================================================
# Part 2: A few more dictionary operations worth knowing
# ============================================================

# --- .update() - merge another dictionary in (adds/overwrites keys) ---
more_contacts = {"Meera": "9000000000", "Sanjay": "9333322211"}
contacts.update(more_contacts)
print("\nAfter .update():", contacts)

# --- .setdefault() - get a value, or set a default if the key is missing ---
# If "Priya" already existed, this would just return her current number.
# Since she doesn't exist yet, it adds her with the default value.
priya_number = contacts.setdefault("Priya", "Unknown")
print("\nAfter .setdefault():", contacts)
print("Priya's number is now:", priya_number)

# --- dict.fromkeys() - build a dictionary from a list, same starting value ---
new_names = ["Ali", "Zoya", "Farhan"]
placeholder_contacts = dict.fromkeys(new_names, "Not added yet")
print("\nPlaceholder contacts from fromkeys():", placeholder_contacts)

# --- Checking if a value exists (not just a key) ---
number_to_check = "9876543210"
if number_to_check in contacts.values():
    print(f"\n{number_to_check} exists in the contact book.")
else:
    print(f"\n{number_to_check} does NOT exist in the contact book.")

# --- Copying a dictionary correctly ---
# This does NOT copy - both point to the SAME dictionary.
wrong_copy = contacts
wrong_copy["Test"] = "0000000000"
print("\nOriginal also changed (aliasing bug):", "Test" in contacts)
del contacts["Test"]

# This DOES copy - a real independent duplicate.
real_copy = contacts.copy()
real_copy["OnlyInCopy"] = "1111111111"
print("Original unaffected:", "OnlyInCopy" in contacts)
print("Copy has the extra entry:", "OnlyInCopy" in real_copy)

# --- Dictionary comprehension ---
# Build a new dictionary from an existing one in one line.
# Example: a dictionary of just the names that start with 'M'
m_names_only = {name: num for name, num in contacts.items() if name.startswith("M")}
print("\nNames starting with 'M' (comprehension):", m_names_only)

# --- Nested dictionary - storing more than one field per contact ---
detailed_contacts = {
    "Kalid": {"phone": "9876543210", "email": "kalid@example.com", "city": "Bengaluru"},
    "Asha": {"phone": "9123456780", "email": "asha@example.com", "city": "Mumbai"},
}

print("\n--- Detailed contact book (nested dictionary) ---")
for name, details in detailed_contacts.items():
    print(f"{name}: {details['phone']}, {details['email']}, {details['city']}")

# --- .clear() - empty a dictionary completely ---
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("\nAfter .clear():", temp_dict)


# ============================================================
# Interactive part: let the user add their own contact
# ============================================================
print("\n--- Add a new contact ---")
new_name = input("Enter a name: ")
new_number = input("Enter a phone number: ")
contacts[new_name] = new_number

print("\nFinal contact book:")
for name, number in contacts.items():
    print(f"{name}: {number}")


# ============================================================
# Part 3: Even more dictionary operations
# ============================================================

# --- Merge operator | (Python 3.9+) - modern alternative to .update() ---
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 20, "z": 3}
merged = dict_a | dict_b  # dict_b's values win on overlapping keys
print("\nMerged with | operator:", merged)

# |= updates a dictionary in place, similar to .update()
dict_a |= dict_b
print("dict_a after |=:", dict_a)

# --- .popitem() - removes and returns the LAST inserted key-value pair ---
sample_dict = {"one": 1, "two": 2, "three": 3}
last_item = sample_dict.popitem()
print("\nRemoved with popitem():", last_item)
print("Dictionary after popitem():", sample_dict)

# --- Dictionary equality comparison ---
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}  # same content, different insertion order
print("\ndict1 == dict2:", dict1 == dict2)  # True - order doesn't matter for equality

# --- KeyError handling with try/except ---
# Accessing a missing key directly (not with .get()) raises a KeyError.
try:
    print(contacts["DoesNotExist"])
except KeyError:
    print("\nThat contact does not exist (caught with try/except).")

# --- Using .get() for counting - a very common real pattern ---
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print("\nWord frequency count:", word_counts)

# --- Sorting a dictionary by key or by value ---
# sorted() on a dict's .items() returns a list of (key, value) tuples.
sorted_by_key = sorted(word_counts.items())
print("\nSorted by key:", sorted_by_key)

sorted_by_value = sorted(word_counts.items(), key=lambda pair: pair[1], reverse=True)
print("Sorted by value (highest count first):", sorted_by_value)

# --- Dictionary keys must be immutable ---
# Strings, numbers, and tuples work fine as keys.
valid_key_example = {("Kalid", "Bengaluru"): "9876543210"}
print("\nTuple as a dictionary key works:", valid_key_example)

# Lists CANNOT be used as keys because they are mutable - this would raise a TypeError:
# invalid_dict = {["Kalid", "Bengaluru"]: "9876543210"}
print("Lists cannot be used as dictionary keys (would raise TypeError).")