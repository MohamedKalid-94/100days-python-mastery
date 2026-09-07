# Day 05 - Countdown Timer
# Concept: Loops (For & While)
# Goal: Practice using for loops and while loops to count down

import time  # lets us pause execution using time.sleep()

# --- Version 1: Countdown using a FOR loop ---
print("--- Countdown using a for loop ---")

start_number = int(input("Enter a number to count down from: "))

# range(start, stop, step) -> counts from start_number down to 1
# stop is 0 because range() is exclusive of the end value
# step is -1 because we're counting DOWN
for i in range(start_number, 0, -1):
    print(i)
    time.sleep(1)  # pause for 1 second between counts

print("Liftoff! 🚀\n")

# --- Version 2: Same countdown using a WHILE loop ---
print("--- Countdown using a while loop ---")

count = start_number

while count > 0:
    print(count)
    time.sleep(1)
    count -= 1  # same as count = count - 1

print("Liftoff! 🚀\n")

# --- Bonus: for loop counting UP instead of down ---
print("--- Bonus: counting up with a for loop ---")
for i in range(1, start_number + 1):
    print(i)

# --- Bonus: using break to stop a loop early ---
print("\n--- Bonus: while loop with a break condition ---")
count = start_number
while True:
    print(count)
    if count == 3:
        print("Stopping early at 3!")
        break
    count -= 1

# --- Bonus: using continue to skip a value ---
print("\n--- Bonus: for loop skipping a specific number with continue ---")
for i in range(start_number, 0, -1):
    if i == 2:
        continue  # skip printing 2
    print(i)