# Day 16 - Daily Journal Logger
# Concept: Writing Files
# Goal: Practice different ways of writing data to a text file

import datetime  # to timestamp each journal entry

# --- Method 1: "w" mode - write (creates the file, OVERWRITES if it exists) ---
with open("journal.txt", "w") as file:
    file.write("Daily Journal\n")
    file.write("=============\n")

print("Journal file created with a header.")

# --- Method 2: "a" mode - append (adds to the end, does NOT overwrite) ---
with open("journal.txt", "a") as file:
    file.write("Entry 1: Started learning Python today.\n")

print("First entry appended.")

# --- Writing multiple lines at once using .writelines() ---
more_entries = [
    "Entry 2: Practiced writing to files.\n",
    "Entry 3: Learned the difference between w and a mode.\n",
]
with open("journal.txt", "a") as file:
    file.writelines(more_entries)

print("Multiple entries appended with .writelines().")

# --- Writing with a timestamp - a realistic journal feature ---
def write_journal_entry(entry_text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal.txt", "a") as file:
        file.write(f"[{timestamp}] {entry_text}\n")

write_journal_entry("Learned how to timestamp journal entries.")
print("Timestamped entry added.")

# --- Writing numbers/other data types - must convert to string first ---
word_count = 42
# file.write(word_count)          # this would raise a TypeError - write() needs a string
with open("journal.txt", "a") as file:
    file.write(f"Word count today: {str(word_count)}\n")

# --- Using print() to write to a file (alternative to .write()) ---
with open("journal.txt", "a") as file:
    print("Entry written using print() with file= argument.", file=file)

print("Entry added using print(file=...).")

# --- Reading back the file to confirm everything was written correctly ---
print("\n--- Current journal contents ---")
with open("journal.txt", "r") as file:
    print(file.read())


# ============================================================
# A proper journal logger function
# ============================================================
def log_entry():
    entry = input("Write your journal entry: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("journal.txt", "a") as file:
        file.write(f"[{timestamp}] {entry}\n")

    print("Entry saved!")


# ============================================================
# Interactive part: keep logging entries until the user is done
# ============================================================
print("\n--- Daily Journal Logger ---")
while True:
    log_entry()
    again = input("Add another entry? (y/n): ")
    if again.lower() != "y":
        break

print("\n--- Final journal contents ---")
with open("journal.txt", "r") as file:
    print(file.read())