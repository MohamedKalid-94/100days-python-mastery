# Day 14 - Random Password Generator
# Concept: Modules & Libraries
# Goal: Practice importing and using built-in Python modules

# --- Importing built-in modules ---
import random
import string

# --- The 'string' module gives us ready-made character sets ---
print("Lowercase letters:", string.ascii_lowercase)
print("Uppercase letters:", string.ascii_uppercase)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)

# --- Combining character sets into one pool to choose from ---
all_characters = string.ascii_letters + string.digits + string.punctuation
print("\nFull character pool:", all_characters)

# --- The 'random' module: picking random characters ---
# random.choice() picks ONE random item from a sequence
random_char = random.choice(all_characters)
print("\nOne random character:", random_char)

# --- Building a password using a for loop ---
password_length = 12
password = ""
for i in range(password_length):
    password += random.choice(all_characters)

print(f"\nGenerated password (for loop): {password}")

# --- Same thing using a list comprehension, then joining it ---
password_comprehension = "".join(random.choice(all_characters) for i in range(password_length))
print(f"Generated password (comprehension): {password_comprehension}")

# --- random.sample() - picks multiple UNIQUE items, no repeats ---
unique_chars = random.sample(string.ascii_letters, 5)
print("\n5 unique random letters (no repeats):", unique_chars)

# --- random.randint() - a random whole number between two values ---
random_number = random.randint(1000, 9999)
print("Random 4-digit number:", random_number)

# --- random.shuffle() - shuffles a list in place ---
digits_list = list(string.digits)
random.shuffle(digits_list)
print("Shuffled digits:", digits_list)


# ============================================================
# A proper password generator function
# ============================================================
def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if character_pool == "":
        return "Error: at least one character type must be selected."

    password = "".join(random.choice(character_pool) for i in range(length))
    return password


# --- Using the function with different options ---
print("\n--- Password generator examples ---")
print("Default (12 chars, all types):", generate_password())
print("Letters only, 8 chars:", generate_password(length=8, use_digits=False, use_symbols=False))
print("Digits only, 6 chars (like a PIN):", generate_password(length=6, use_letters=False, use_symbols=False))
print("No symbols, 16 chars:", generate_password(length=16, use_symbols=False))


# ============================================================
# Interactive part: let the user customize their password
# ============================================================
print("\n--- Create your own password ---")
length = int(input("Enter desired password length: "))
include_letters = input("Include letters? (y/n): ").lower() == "y"
include_digits = input("Include digits? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

final_password = generate_password(length, include_letters, include_digits, include_symbols)
print(f"\nYour generated password: {final_password}")


# ============================================================
# Part 2: The secrets module - the CORRECT tool for real passwords
# ============================================================
# random is fine for games, simulations, and shuffling things -
# but it is NOT cryptographically secure. Its output can, in some
# cases, be predicted by an attacker who studies enough of it.
#
# For anything security-related (passwords, tokens, API keys),
# Python provides the 'secrets' module instead. Use secrets, not
# random, whenever the output actually needs to be unguessable.

import secrets

# --- secrets.choice() - same idea as random.choice(), but secure ---
secure_char = secrets.choice(all_characters)
print("\nOne secure random character:", secure_char)

# --- Building a secure password using secrets.choice() ---
def generate_secure_password(length=12):
    return "".join(secrets.choice(all_characters) for i in range(length))

secure_password = generate_secure_password(12)
print("Secure password (secrets module):", secure_password)

# --- secrets.token_urlsafe() - generates a ready-to-use secure random token/string ---
# Useful for things like session tokens, password reset links, API keys.
url_token = secrets.token_urlsafe(16)
print("\nURL-safe secure token:", url_token)

# --- secrets.token_hex() - a secure random token in hexadecimal format ---
hex_token = secrets.token_hex(16)
print("Hex secure token:", hex_token)

print("\nRule of thumb: use 'random' for games and simulations,")
print("use 'secrets' for anything security-related, like real passwords.")