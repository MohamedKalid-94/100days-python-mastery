# Day 17 - Student Report Generator
# Concept: CSV Files
# Goal: Practice reading from and writing to CSV files using the csv module

import csv

# --- Writing data to a CSV file using csv.writer ---
students = [
    ["Name", "Subject", "Marks"],   # header row
    ["Kalid", "Python", 88],
    ["Asha", "Python", 92],
    ["Ravi", "Python", 75],
    ["Meera", "Python", 60],
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)   # writes all rows at once

print("students.csv created.\n")

# --- Writing a single row at a time with .writerow() ---
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sanjay", "Python", 81])

print("Added one more student with .writerow().\n")

# --- Reading a CSV file using csv.reader ---
print("--- Reading with csv.reader ---")
with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)   # each row is a plain list of strings

# --- Skipping the header row while reading ---
print("\n--- Reading data rows only (skipping header) ---")
with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)   # grabs the first row and advances past it
    print("Header:", header)

    for row in reader:
        name, subject, marks = row
        print(f"{name} scored {marks} in {subject}")

# --- Using csv.DictReader - reads each row as a dictionary (much more useful) ---
print("\n--- Reading with csv.DictReader ---")
with open("students.csv", "r", newline="") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row)   # row is now a dictionary, e.g. {'Name': 'Kalid', 'Subject': 'Python', 'Marks': '88'}

# --- Using csv.DictWriter - write rows from dictionaries instead of lists ---
new_students = [
    {"Name": "Priya", "Subject": "Python", "Marks": 95},
    {"Name": "Ali", "Subject": "Python", "Marks": 70},
]

with open("students.csv", "a", newline="") as file:
    fieldnames = ["Name", "Subject", "Marks"]
    dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    dict_writer.writerows(new_students)   # note: no header written since file already has one

print("\nAdded more students using DictWriter.")

# --- Note: values from CSV are always read as strings - must convert manually ---
with open("students.csv", "r", newline="") as file:
    dict_reader = csv.DictReader(file)
    marks_list = [int(row["Marks"]) for row in dict_reader]

print("\nMarks as actual integers:", marks_list)
print("Average marks:", sum(marks_list) / len(marks_list))


# ============================================================
# A student report generator using the CSV data
# ============================================================
def generate_report():
    with open("students.csv", "r", newline="") as file:
        dict_reader = csv.DictReader(file)
        students_data = list(dict_reader)

    print("\n--- Student Report ---")
    for student in students_data:
        marks = int(student["Marks"])
        status = "Pass" if marks >= 50 else "Fail"
        print(f"{student['Name']:<10} | {student['Subject']:<10} | {marks:>3} | {status}")

    all_marks = [int(s["Marks"]) for s in students_data]
    print(f"\nClass average: {sum(all_marks) / len(all_marks):.2f}")
    print(f"Highest score: {max(all_marks)}")
    print(f"Lowest score: {min(all_marks)}")


generate_report()


# ============================================================
# Interactive part: add a new student to the CSV
# ============================================================
print("\n--- Add a new student ---")
new_name = input("Enter student name: ")
new_marks = input("Enter marks: ")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([new_name, "Python", new_marks])

print("\nStudent added. Updated report:")
generate_report()