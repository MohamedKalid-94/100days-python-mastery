# Day 18 - Mini To-Do App
# Concept: JSON Files
# Goal: Practice reading from and writing to JSON files using the json module

import json

# --- Python data (a list of dictionaries) representing to-do items ---
todos = [
    {"task": "Learn Python basics", "done": True},
    {"task": "Build a to-do app", "done": False},
    {"task": "Practice JSON files", "done": False},
]

# --- Writing Python data to a JSON file using json.dump() ---
with open("todos.json", "w") as file:
    json.dump(todos, file)

print("todos.json created.\n")

# --- Writing with indent= for a nicely formatted, human-readable file ---
with open("todos.json", "w") as file:
    json.dump(todos, file, indent=4)

print("todos.json rewritten with indent=4 (pretty-printed).\n")

# --- Reading a JSON file back into Python using json.load() ---
with open("todos.json", "r") as file:
    loaded_todos = json.load(file)

print("--- Loaded from JSON ---")
print(loaded_todos)
print("Type of loaded data:", type(loaded_todos))

# --- The loaded data is normal Python again - lists, dicts, etc. ---
for todo in loaded_todos:
    status = "Done" if todo["done"] else "Pending"
    print(f"{todo['task']} - {status}")

# --- json.dumps() - convert Python data to a JSON STRING (not a file) ---
json_string = json.dumps(todos, indent=2)
print("\n--- As a JSON string (json.dumps) ---")
print(json_string)
print("Type:", type(json_string))

# --- json.loads() - convert a JSON STRING back into Python data ---
parsed_back = json.loads(json_string)
print("\n--- Parsed back from string (json.loads) ---")
print(parsed_back[0])

# --- JSON only supports certain data types ---
# Matches Python: dict, list, str, int, float, bool (True/False), None
# JSON uses: object, array, string, number, number, true/false, null
sample_data = {
    "name": "Kalid",
    "age": 30,
    "height": 1.76,
    "is_learning": True,
    "middle_name": None,
}
print("\nSample with mixed types:", json.dumps(sample_data, indent=2))


# ============================================================
# A proper to-do manager using JSON as storage
# ============================================================
def load_todos():
    try:
        with open("todos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []   # no file yet, start with an empty list


def save_todos(todos_list):
    with open("todos.json", "w") as file:
        json.dump(todos_list, file, indent=4)


def add_todo(task_text):
    todos_list = load_todos()
    todos_list.append({"task": task_text, "done": False})
    save_todos(todos_list)


def mark_done(task_text):
    todos_list = load_todos()
    for todo in todos_list:
        if todo["task"] == task_text:
            todo["done"] = True
    save_todos(todos_list)


def show_todos():
    todos_list = load_todos()
    print("\n--- To-Do List ---")
    for todo in todos_list:
        status = "[x]" if todo["done"] else "[ ]"
        print(f"{status} {todo['task']}")


# --- Using the functions together ---
show_todos()
add_todo("Learn about JSON persistence")
mark_done("Learn Python basics")
show_todos()


# ============================================================
# Interactive part: add and manage your own to-dos
# ============================================================
print("\n--- Mini To-Do App ---")
while True:
    print("\n1. Show to-dos")
    print("2. Add a to-do")
    print("3. Mark a to-do as done")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_todos()
    elif choice == "2":
        new_task = input("Enter the new task: ")
        add_todo(new_task)
        print("Task added.")
    elif choice == "3":
        task_to_complete = input("Enter the task to mark as done: ")
        mark_done(task_to_complete)
        print("Task updated.")
    elif choice == "4":
        break
    else:
        print("Invalid option.")

print("\nGoodbye!")