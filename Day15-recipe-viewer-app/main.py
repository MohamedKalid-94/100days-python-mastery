# Day 15 - Recipe Viewer App
# Concept: Reading Files
# Goal: Practice different ways of reading data from a text file

# --- First, create a sample recipes file to read from ---
with open("recipes.txt", "w") as file:
    file.write("Pancakes\n")
    file.write("Ingredients: Flour, Milk, Eggs, Sugar\n")
    file.write("Steps: Mix ingredients, pour batter, cook until golden\n")
    file.write("---\n")
    file.write("Omelette\n")
    file.write("Ingredients: Eggs, Salt, Pepper, Butter\n")
    file.write("Steps: Beat eggs, cook in butter, fold and serve\n")
    file.write("---\n")
    file.write("Salad\n")
    file.write("Ingredients: Lettuce, Tomato, Cucumber, Dressing\n")
    file.write("Steps: Chop vegetables, mix, add dressing\n")

print("Sample recipes.txt file created.\n")

# --- Method 1: .read() - read the ENTIRE file as one string ---
with open("recipes.txt", "r") as file:
    full_content = file.read()

print("--- Method 1: .read() ---")
print(full_content)

# --- Method 2: .readline() - read ONE line at a time ---
print("--- Method 2: .readline() ---")
with open("recipes.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print("First line:", first_line.strip())
    print("Second line:", second_line.strip())

# --- Method 3: .readlines() - read ALL lines into a list ---
print("\n--- Method 3: .readlines() ---")
with open("recipes.txt", "r") as file:
    all_lines = file.readlines()

print("Number of lines:", len(all_lines))
print("Third line from the list:", all_lines[2].strip())

# --- Method 4: looping directly over the file object (most common/efficient way) ---
print("\n--- Method 4: looping over the file directly ---")
with open("recipes.txt", "r") as file:
    for line in file:
        print(line.strip())

# --- Filtering while reading: only print lines that mention "Ingredients" ---
print("\n--- Only ingredient lines ---")
with open("recipes.txt", "r") as file:
    for line in file:
        if line.startswith("Ingredients"):
            print(line.strip())

# --- Splitting the file into separate recipes using the "---" separator ---
with open("recipes.txt", "r") as file:
    content = file.read()

recipes = content.strip().split("---\n")
print(f"\nFound {len(recipes)} recipes in the file.")

for index, recipe in enumerate(recipes, start=1):
    print(f"\nRecipe {index}:")
    print(recipe.strip())


# ============================================================
# Interactive part: search for a recipe by name
# ============================================================
print("\n--- Search for a recipe ---")
search_term = input("Enter a recipe name to search for: ")

found = False
with open("recipes.txt", "r") as file:
    content = file.read()

recipes = content.strip().split("---\n")
for recipe in recipes:
    if search_term.lower() in recipe.lower():
        print(f"\nFound:\n{recipe.strip()}")
        found = True
        break

if not found:
    print(f"\nNo recipe found matching '{search_term}'.")