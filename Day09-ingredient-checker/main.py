# Day 09 - Ingredient Checker
# Concept: Tuples & Sets
# Goal: Practice working with tuples (fixed, ordered data) and sets (unique, unordered data)

# ============================================================
# Part 1: Tuples
# ============================================================
# Tuples are like lists, but immutable (cannot be changed after creation).
# Good for fixed data that shouldn't change, e.g. a recipe's core ingredients.

recipe_ingredients = ("Flour", "Sugar", "Eggs", "Butter")
print("Recipe ingredients (tuple):", recipe_ingredients)

# --- Accessing items by index (same as lists) ---
print("First ingredient:", recipe_ingredients[0])
print("Last ingredient:", recipe_ingredients[-1])

# --- Tuples cannot be modified - this would raise an error ---
# recipe_ingredients[0] = "Rice"   # TypeError: 'tuple' object does not support item assignment
print("\nTuples are immutable - you cannot change an item after creation.")

# --- Looping through a tuple ---
print("\n--- Looping through the tuple ---")
for ingredient in recipe_ingredients:
    print(ingredient)

# --- Checking membership with 'in' ---
check = "Eggs"
if check in recipe_ingredients:
    print(f"\n'{check}' is required for this recipe.")

# --- Tuple unpacking ---
first, second, third, fourth = recipe_ingredients
print(f"\nUnpacked: {first}, {second}, {third}, {fourth}")

# --- Tuples can be used as dictionary keys (unlike lists) ---
coordinates_data = {(0, 0): "origin", (1, 1): "diagonal point"}
print("\nTuple as a dict key:", coordinates_data[(0, 0)])


# ============================================================
# Part 2: Sets
# ============================================================
# Sets store UNIQUE items only, with no guaranteed order.
# Good for checking "what ingredients do I have" without duplicates.

pantry = {"Flour", "Sugar", "Eggs", "Milk", "Salt"}
print("\nPantry (set):", pantry)

# --- Adding an item ---
pantry.add("Butter")
print("\nAfter adding Butter:", pantry)

# --- Adding a duplicate does nothing (sets only keep unique items) ---
pantry.add("Sugar")
print("After adding Sugar again (already existed):", pantry)

# --- Removing an item ---
pantry.remove("Salt")
print("\nAfter removing Salt:", pantry)

# --- Checking membership with 'in' (very fast for sets) ---
item_to_check = "Milk"
if item_to_check in pantry:
    print(f"\n'{item_to_check}' is in the pantry.")
else:
    print(f"\n'{item_to_check}' is NOT in the pantry.")

# --- Set operations: comparing what's needed vs what's available ---
needed = set(recipe_ingredients)
print("\nNeeded ingredients (as a set):", needed)
print("Available in pantry:", pantry)

# Intersection: ingredients we need AND already have
have = needed & pantry
print("\nIngredients we already have:", have)

# Difference: ingredients we need but DON'T have (still need to buy)
missing = needed - pantry
print("Ingredients still needed (missing):", missing)

# Union: all ingredients combined (needed + pantry, no duplicates)
all_ingredients = needed | pantry
print("All ingredients combined:", all_ingredients)

# Symmetric difference: items in only ONE of the two sets, not both
only_in_one = needed ^ pantry
print("Items only in one set (not shared):", only_in_one)

# --- Checking if we have everything we need ---
if needed.issubset(pantry):
    print("\nWe have everything needed for the recipe!")
else:
    print("\nWe're missing some ingredients:", missing)


# ============================================================
# Interactive part: check your own ingredients
# ============================================================
print("\n--- Check your ingredients ---")
user_input = input("Enter the ingredients you have, separated by commas: ")
user_pantry = set(item.strip() for item in user_input.split(","))

still_missing = needed - user_pantry

if not still_missing:
    print("\nGreat! You have everything needed for the recipe.")
else:
    print("\nYou're still missing:", still_missing)


# ============================================================
# Part 3: Even more tuple and set operations
# ============================================================

# --- Tuples: .count() and .index() ---
sample_tuple = ("Flour", "Sugar", "Flour", "Eggs")
print("\n'Flour' appears", sample_tuple.count("Flour"), "times")
print("First position of 'Flour':", sample_tuple.index("Flour"))

# --- Tuples: concatenation (+) and repetition (*) ---
combined_tuple = ("Flour", "Sugar") + ("Eggs", "Butter")
print("\nConcatenated tuple:", combined_tuple)

repeated_tuple = ("Salt",) * 3
print("Repeated tuple:", repeated_tuple)

# --- Single-element tuple syntax - a common trap ---
not_a_tuple = ("Flour")       # this is just a STRING in parentheses
actual_tuple = ("Flour",)     # the trailing comma makes it a real tuple
print("\ntype without comma:", type(not_a_tuple))
print("type with comma:", type(actual_tuple))

# --- Nested tuples ---
recipe_steps = (
    ("Step 1", "Mix flour and sugar"),
    ("Step 2", "Add eggs and butter"),
)
print("\n--- Nested tuple (recipe steps) ---")
for step_num, description in recipe_steps:
    print(f"{step_num}: {description}")

# --- tuple() constructor - converting other iterables ---
list_to_tuple = tuple(["Milk", "Bread", "Eggs"])
print("\nList converted to tuple:", list_to_tuple)

# --- len() on a tuple ---
print("Length of recipe_ingredients tuple:", len(recipe_ingredients))

# --- namedtuple - access fields by name instead of index ---
from collections import namedtuple

Ingredient = namedtuple("Ingredient", ["name", "quantity"])
flour = Ingredient(name="Flour", quantity="2 cups")
print("\nnamedtuple example:", flour)
print("Accessing by name:", flour.name, "-", flour.quantity)


# --- Sets: .discard() vs .remove() ---
demo_set = {"Flour", "Sugar", "Eggs"}
demo_set.discard("NotInSet")  # does nothing, no error
print("\n.discard() on a missing item - no error:", demo_set)

# demo_set.remove("NotInSet")  # this WOULD raise a KeyError

# --- Sets: .pop() removes a random item (sets have no order) ---
popped_item = demo_set.pop()
print(".pop() removed a random item:", popped_item)
print("Set after pop():", demo_set)

# --- Sets: .update() - add multiple items at once ---
demo_set.update(["Butter", "Milk"])
print("\nAfter .update() with multiple items:", demo_set)

# --- Sets: .clear() - empty a set completely ---
temp_set = {"a", "b", "c"}
temp_set.clear()
print("\nAfter .clear():", temp_set)

# --- Sets: .issuperset() - reverse of .issubset() ---
big_set = {"Flour", "Sugar", "Eggs", "Milk", "Butter"}
small_set = {"Flour", "Sugar"}
print("\nbig_set.issuperset(small_set):", big_set.issuperset(small_set))

# --- Sets: .isdisjoint() - check if two sets share nothing in common ---
other_set = {"Chili", "Ginger"}
print("pantry.isdisjoint(other_set):", pantry.isdisjoint(other_set))

# --- frozenset - an immutable set, can be used as a dict key ---
frozen = frozenset(["Flour", "Sugar"])
frozen_as_key = {frozen: "base ingredients"}
print("\nfrozenset used as a dict key:", frozen_as_key)

# --- Set comprehension ---
uppercase_pantry = {item.upper() for item in pantry}
print("\nUppercase pantry (set comprehension):", uppercase_pantry)

# --- Copying a set correctly ---
wrong_copy = pantry
wrong_copy.add("THIS AFFECTS BOTH")
print("\nOriginal also changed (aliasing bug):", "THIS AFFECTS BOTH" in pantry)
pantry.discard("THIS AFFECTS BOTH")

real_copy = pantry.copy()
real_copy.add("Only in the copy")
print("Original unaffected:", "Only in the copy" in pantry)
print("Copy has the extra item:", "Only in the copy" in real_copy)

# --- Sets have no guaranteed order ---
print("\nNote: printing a set may show items in a different order than added.")