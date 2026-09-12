# Day 10 - Note-Taking App
# Concept: File Handling
# Goal: Practice reading from and writing to files

# --- Writing to a file (creates the file if it doesn't exist, overwrites if it does) ---
# "w" mode = write (overwrites existing content)
with open("notes.txt", "w") as file:
    file.write("My First Note\n")
    file.write("This is a note-taking app built on Day 10.\n")

print("Notes file created and written.")

# --- Reading the entire file at once ---
with open("notes.txt", "r") as file:
    content = file.read()

print("\n--- Full file content ---")
print(content)

# --- Appending to a file (adds to the end, doesn't overwrite) ---
# "a" mode = append
with open("notes.txt", "a") as file:
    file.write("Second note added later.\n")

print("Appended a new note.")

# --- Reading a file line by line ---
print("\n--- Reading line by line ---")
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the trailing newline character

# --- Reading all lines into a list ---
with open("notes.txt", "r") as file:
    lines = file.readlines()

print("\n--- Lines as a list ---")
print(lines)
print(f"Total lines: {len(lines)}")

# --- Checking if a file exists before reading (avoids errors) ---
import os

filename = "notes.txt"
if os.path.exists(filename):
    print(f"\n'{filename}' exists.")
else:
    print(f"\n'{filename}' does not exist.")

# --- Handling errors when a file doesn't exist ---
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\n'missing_file.txt' was not found (caught with try/except).")


# ============================================================
# Interactive part: a simple note-taking loop
# ============================================================
print("\n--- Add your own notes ---")
print("Type a note and press Enter. Type 'done' when finished.")

with open("notes.txt", "a") as file:
    while True:
        note = input("Note: ")
        if note.lower() == "done":
            break
        file.write(note + "\n")

print("\n--- All notes saved so far ---")
with open("notes.txt", "r") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}. {line.strip()}")


# ============================================================
# Part 2: A few more file handling operations worth knowing
# ============================================================

# --- "r+" mode - read and write WITHOUT truncating existing content ---
with open("notes.txt", "r+") as file:
    existing = file.read()
    print("\nRead with r+ mode (content preserved):", len(existing), "characters")
    # writing here would insert at the current cursor position, not overwrite from the start

# --- "x" mode - exclusive create, fails if the file already exists ---
try:
    with open("notes.txt", "x") as file:
        file.write("This will never run since notes.txt already exists.")
except FileExistsError:
    print("\n'x' mode raised FileExistsError since notes.txt already exists.")

# --- .writelines() - write multiple lines at once from a list ---
lines_to_add = ["Bulk note 1\n", "Bulk note 2\n", "Bulk note 3\n"]
with open("notes.txt", "a") as file:
    file.writelines(lines_to_add)
print("\nAdded multiple lines at once with .writelines()")

# --- file.seek() and file.tell() - moving and checking the cursor position ---
with open("notes.txt", "r") as file:
    print("\nCursor position at start:", file.tell())
    file.read(20)  # move forward by reading 20 characters
    print("Cursor position after reading 20 chars:", file.tell())
    file.seek(0)  # move cursor back to the beginning
    print("Cursor position after seek(0):", file.tell())

# --- Reading a specific number of characters ---
with open("notes.txt", "r") as file:
    first_ten_chars = file.read(10)
    print("\nFirst 10 characters:", repr(first_ten_chars))

# --- Working with file paths properly using pathlib ---
from pathlib import Path

notes_path = Path("notes.txt")
print("\nUsing pathlib - file name:", notes_path.name)
print("Using pathlib - exists:", notes_path.exists())
print("Using pathlib - absolute path:", notes_path.resolve())

# --- Deleting a file ---
demo_file = Path("temp_demo.txt")
demo_file.write_text("temporary content")
print("\nCreated a temporary demo file:", demo_file.exists())

demo_file.unlink()  # same as os.remove("temp_demo.txt")
print("Deleted the temporary demo file. Exists now:", demo_file.exists())

# --- Binary mode - for non-text files like images ---
# "wb" = write binary, "rb" = read binary
with open("demo_binary.bin", "wb") as file:
    file.write(b"\x00\x01\x02\x03")  # raw bytes, not text

with open("demo_binary.bin", "rb") as file:
    binary_content = file.read()
print("\nBinary file content:", binary_content)

Path("demo_binary.bin").unlink()  # clean up the demo file

# --- Context manager with multiple files at once ---
with open("notes.txt", "r") as source, open("notes_backup.txt", "w") as backup:
    backup.write(source.read())
print("\nCopied notes.txt into notes_backup.txt using two files in one 'with' statement.")