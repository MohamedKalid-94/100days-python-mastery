# Day 13 - Student Grade Manager
# Concept: List Comprehensions
# Goal: Practice building new lists from existing ones in a single, readable line

# --- A list of student scores ---
scores = [55, 82, 91, 40, 67, 78, 100, 35, 60, 88]
print("All scores:", scores)

# --- The "old way": building a new list using a for loop ---
passed_loop = []
for score in scores:
    if score >= 50:
        passed_loop.append(score)
print("\nPassed scores (using a for loop):", passed_loop)

# --- The SAME result using a list comprehension ---
# Syntax: [expression for item in iterable if condition]
passed_comprehension = [score for score in scores if score >= 50]
print("Passed scores (using a list comprehension):", passed_comprehension)

# --- List comprehension WITHOUT a condition - just transforming each item ---
# Convert each score into a percentage string
percentages = [f"{score}%" for score in scores]
print("\nScores as percentages:", percentages)

# --- List comprehension that converts each score into a letter grade ---
def score_to_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

grades = [score_to_grade(score) for score in scores]
print("\nLetter grades:", grades)

# --- Combining scores and grades using zip() inside a comprehension ---
score_grade_pairs = [(score, score_to_grade(score)) for score in scores]
print("\nScore-grade pairs:", score_grade_pairs)

# --- List comprehension with an if-else (different from if-only filtering) ---
# Note the position: "expression if condition else other_expression"
pass_fail_labels = ["Pass" if score >= 50 else "Fail" for score in scores]
print("\nPass/Fail labels:", pass_fail_labels)

# --- Nested list comprehension - flattening a list of lists ---
students_scores = [[85, 90], [60, 70], [40, 55]]
flattened = [score for student in students_scores for score in student]
print("\nFlattened nested scores:", flattened)

# --- Dictionary comprehension (related concept, very common alongside list comprehensions) ---
student_names = ["Kalid", "Asha", "Ravi", "Meera", "Sanjay", "Priya", "Ali", "Zoya", "Farhan", "Rani"]
student_grades = {name: score_to_grade(score) for name, score in zip(student_names, scores)}
print("\nStudent grades (dict comprehension):", student_grades)

# --- Set comprehension - unique grades that appear ---
unique_grades = {score_to_grade(score) for score in scores}
print("\nUnique grades present:", unique_grades)

# --- Using comprehensions with built-in functions like sum(), len(), max() ---
average_score = sum(scores) / len(scores)
print(f"\nAverage score: {average_score:.2f}")
print("Highest score:", max(scores))
print("Lowest score:", min(scores))

# --- Comprehension to count how many students passed ---
num_passed = len([score for score in scores if score >= 50])
print(f"\nNumber of students who passed: {num_passed} out of {len(scores)}")


# ============================================================
# Interactive part: check a student's grade
# ============================================================
print("\n--- Check a student's grade ---")
student_name = input("Enter a student name: ")

if student_name in student_grades:
    print(f"{student_name}'s grade: {student_grades[student_name]}")
else:
    print(f"No record found for '{student_name}'.")