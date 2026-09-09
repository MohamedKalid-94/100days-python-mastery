# Day 07 - Shopping List App
# Concept: Lists
# Goal: Practice creating, updating, and working with Python lists

# --- Creating an empty list ---
shopping_list = []

# --- Adding items with .append() ---
shopping_list.append("Milk")
shopping_list.append("Eggs")
shopping_list.append("Bread")
print("After adding items:", shopping_list)

# --- Adding an item at a specific position with .insert() ---
shopping_list.insert(1, "Butter")  # inserts "Butter" at index 1
print("After inserting Butter at index 1:", shopping_list)

# --- Removing an item by value with .remove() ---
shopping_list.remove("Eggs")
print("After removing Eggs:", shopping_list)

# --- Removing the last item with .pop() (also returns the removed item) ---
removed_item = shopping_list.pop()
print(f"Removed last item: {removed_item}")
print("List now:", shopping_list)

# --- Checking if an item exists using 'in' ---
item_to_check = "Milk"
if item_to_check in shopping_list:
    print(f"'{item_to_check}' is in the list.")
else:
    print(f"'{item_to_check}' is NOT in the list.")

# --- Looping through the list with a for loop ---
print("\n--- Full shopping list ---")
for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")

# --- List length using len() ---
print(f"\nTotal items in list: {len(shopping_list)}")

# --- Sorting the list alphabetically ---
shopping_list.sort()
print("Sorted list:", shopping_list)

# --- Slicing: getting a portion of the list ---
print("First two items:", shopping_list[0:2])
print("Last item:", shopping_list[-1])

# --- Interactive part: let the user add their own items ---
print("\n--- Add your own items ---")
while True:
    new_item = input("Enter an item to add (or 'done' to finish): ")
    if new_item.lower() == "done":
        break
    shopping_list.append(new_item)

print("\nFinal shopping list:")
for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")


# ============================================================
# Part 2: A few more list operations worth knowing
# ============================================================

# --- .extend() vs .append() ---
# append() adds ONE item (even a list gets added as a single element)
# extend() merges another list's items in individually
more_items = ["Cheese", "Yogurt"]
shopping_list.extend(more_items)
print("\nAfter .extend():", shopping_list)

# --- .count() - how many times an item appears ---
sample_list = ["Milk", "Bread", "Milk", "Eggs", "Milk"]
print("\n'Milk' appears", sample_list.count("Milk"), "times")

# --- .index() - find the position of an item ---
print("First position of 'Milk':", sample_list.index("Milk"))

# --- .reverse() - reverse the list in place ---
shopping_list.reverse()
print("\nReversed list:", shopping_list)
shopping_list.reverse()  # reverse back for the rest of the demo

# --- del list[index] - remove an item by position ---
print("\nBefore del:", shopping_list)
del shopping_list[0]
print("After deleting index 0:", shopping_list)

# --- List comprehension - build a new list in one line ---
uppercase_items = [item.upper() for item in shopping_list]
print("\nUppercase items (comprehension):", uppercase_items)

# comprehension with a condition
short_names = [item for item in shopping_list if len(item) <= 5]
print("Items with 5 or fewer letters:", short_names)

# --- Copying a list correctly ---
# This does NOT copy - both point to the SAME list.
wrong_copy = shopping_list
wrong_copy.append("THIS AFFECTS BOTH")
print("\nOriginal also changed (aliasing bug):", shopping_list)
shopping_list.remove("THIS AFFECTS BOTH")

# This DOES copy - a real independent duplicate.
real_copy = shopping_list.copy()  # or shopping_list[:]
real_copy.append("Only in the copy")
print("Original unaffected:", shopping_list)
print("Copy has the extra item:", real_copy)

# --- .clear() - empty the whole list at once ---
temp_list = ["a", "b", "c"]
temp_list.clear()
print("\nAfter .clear():", temp_list)

# --- zip() - combining two related lists together ---
names = ["Milk", "Bread", "Eggs"]
quantities = [2, 1, 12]
for name, qty in zip(names, quantities):
    print(f"\n{name}: {qty}")

# --- Nested lists (2D) - a small table of data ---
receipt_table = [
    ["Milk", 2, 60],
    ["Bread", 1, 40],
]
print("\n--- Nested list (table) ---")
for row in receipt_table:
    item, qty, price = row
    print(f"{item}: qty {qty}, price {price}")

# --- sorted() with key= - sort by something other than default order ---
sorted_by_length = sorted(shopping_list, key=len)
print("\nSorted by word length:", sorted_by_length)

# --- min() / max() / sum() - common aggregate operations ---
numbers = [4, 8, 2, 10, 6]
print("\nmin():", min(numbers))
print("max():", max(numbers))
print("sum():", sum(numbers))

# --- List multiplication - quickly create a list of repeated values ---
zeros = [0] * 5
print("\nList multiplication [0] * 5:", zeros)

# --- Checking if a list is empty ---
empty_list = []
if not empty_list:
    print("\nempty_list is empty (checked with 'not').")