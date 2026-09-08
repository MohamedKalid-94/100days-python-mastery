# Day 06 - Math Quiz Game
# Concept: Functions
# Goal: Practice defining and calling functions, using parameters and return values

import random  # to generate random numbers for the quiz questions


# --- A function that generates a random math question ---
# Returns three things: the question text, and the correct answer
def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    question_text = f"{num1} {operator} {num2}"
    return question_text, answer  # returning multiple values as a tuple


# --- A function that asks one question and checks the answer ---
# Takes parameters (question, correct_answer) and returns True/False
def ask_question(question, correct_answer):
    user_input = input(f"What is {question}? ")

    # Basic validation: make sure the input is a number
    if not user_input.lstrip("-").isdigit():
        print("That's not a valid number. Marked as incorrect.")
        return False

    user_answer = int(user_input)

    if user_answer == correct_answer:
        print("Correct! ✅")
        return True
    else:
        print(f"Wrong. The correct answer was {correct_answer}. ❌")
        return False


# --- A function that runs the full quiz ---
# Takes a parameter for how many questions to ask
def run_quiz(num_questions):
    score = 0

    for i in range(1, num_questions + 1):
        print(f"\nQuestion {i} of {num_questions}")
        question, answer = generate_question()

        if ask_question(question, answer):
            score += 1

    return score


# --- A function to print a summary message based on the score ---
def show_result(score, total):
    print(f"\n--- Quiz Finished ---")
    print(f"You scored {score} out of {total}")

    percentage = (score / total) * 100

    if percentage == 100:
        print("Perfect score! 🎉")
    elif percentage >= 70:
        print("Great job!")
    elif percentage >= 40:
        print("Not bad, keep practicing.")
    else:
        print("Keep practicing, you'll get better!")


# --- Main program: this is where functions are actually called ---
if __name__ == "__main__":
    print("Welcome to the Math Quiz Game!")
    num_questions = int(input("How many questions would you like? "))

    final_score = run_quiz(num_questions)
    show_result(final_score, num_questions)