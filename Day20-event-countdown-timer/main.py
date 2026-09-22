# Day 20 - Event Countdown Timer
# Concept: Dates & Time
# Goal: Practice working with the datetime module

import datetime

# --- Getting the current date and time ---
now = datetime.datetime.now()
print("Current date and time:", now)
print("Type:", type(now))

# --- Getting just the current date (no time) ---
today = datetime.date.today()
print("\nToday's date:", today)

# --- Accessing individual parts of a datetime object ---
print("\n--- Breaking down 'now' ---")
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Weekday (0=Monday):", now.weekday())

# --- Creating a specific date/datetime manually ---
new_year = datetime.datetime(2027, 1, 1, 0, 0, 0)
print("\nA specific event date:", new_year)

# --- Formatting dates into readable strings with strftime() ---
# %Y = 4-digit year, %m = month, %d = day, %H = hour, %M = minute, %S = second
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("\nFormatted with strftime:", formatted)

readable = now.strftime("%A, %B %d, %Y")   # e.g. "Saturday, September 05, 2026"
print("Readable format:", readable)

# --- Parsing a string INTO a datetime object with strptime() ---
date_string = "2026-12-25"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("\nParsed from string:", parsed_date)

# --- Calculating the difference between two dates - a timedelta ---
event_date = datetime.datetime(2026, 12, 25, 0, 0, 0)
time_remaining = event_date - now

print(f"\nTime remaining until {event_date.strftime('%B %d, %Y')}:")
print(time_remaining)
print("Type:", type(time_remaining))

# --- Breaking a timedelta down into days, hours, minutes ---
days = time_remaining.days
total_seconds = time_remaining.seconds   # seconds remaining AFTER full days
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60

print(f"\n{days} days, {hours} hours, {minutes} minutes remaining.")

# --- Adding/subtracting time using timedelta ---
one_week_later = now + datetime.timedelta(weeks=1)
print("\nOne week from now:", one_week_later.strftime("%Y-%m-%d"))

ten_days_ago = now - datetime.timedelta(days=10)
print("Ten days ago:", ten_days_ago.strftime("%Y-%m-%d"))

# --- Comparing dates directly ---
if event_date > now:
    print(f"\n{event_date.strftime('%B %d')} is in the future.")
else:
    print(f"\n{event_date.strftime('%B %d')} has already passed.")


# ============================================================
# A reusable countdown function
# ============================================================
def countdown_to(event_name, event_date_str, date_format="%Y-%m-%d"):
    event_dt = datetime.datetime.strptime(event_date_str, date_format)
    now = datetime.datetime.now()

    if event_dt < now:
        return f"{event_name} has already happened."

    remaining = event_dt - now
    days = remaining.days
    hours = remaining.seconds // 3600
    minutes = (remaining.seconds % 3600) // 60

    return f"{event_name} is in {days} days, {hours} hours, and {minutes} minutes."


print("\n" + countdown_to("New Year", "2027-01-01"))
print(countdown_to("Christmas", "2026-12-25"))


# ============================================================
# Interactive part: countdown to a user-chosen event
# ============================================================
print("\n--- Create your own countdown ---")
event_name = input("Enter the event name: ")
event_date_input = input("Enter the event date (YYYY-MM-DD): ")

try:
    result = countdown_to(event_name, event_date_input)
    print(f"\n{result}")
except ValueError:
    print("\nInvalid date format. Please use YYYY-MM-DD.")


# ============================================================
# Part 2: Timezones - the one that actually matters in real apps
# ============================================================
# Everything above was "naive" datetime - it has no idea what timezone
# it belongs to. This is fine for local scripts, but breaks down the
# moment your code deals with users in different locations, or runs
# on a server (which is often set to UTC, not your local time).

from zoneinfo import ZoneInfo

# --- Getting the current time in a SPECIFIC timezone ---
utc_now = datetime.datetime.now(ZoneInfo("UTC"))
india_now = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
new_york_now = datetime.datetime.now(ZoneInfo("America/New_York"))

print("\n--- Same moment, different timezones ---")
print("UTC:      ", utc_now.strftime("%Y-%m-%d %H:%M:%S %Z"))
print("India:    ", india_now.strftime("%Y-%m-%d %H:%M:%S %Z"))
print("New York: ", new_york_now.strftime("%Y-%m-%d %H:%M:%S %Z"))

# --- Converting an "aware" datetime from one timezone to another ---
converted_to_ny = india_now.astimezone(ZoneInfo("America/New_York"))
print("\nIndia time converted to New York time:", converted_to_ny.strftime("%Y-%m-%d %H:%M:%S %Z"))

# --- Naive vs aware datetimes cannot be compared or subtracted directly ---
naive_dt = datetime.datetime(2026, 12, 25)          # no timezone info - "naive"
aware_dt = datetime.datetime(2026, 12, 25, tzinfo=ZoneInfo("UTC"))  # has timezone - "aware"

try:
    difference = aware_dt - naive_dt
except TypeError as error:
    print(f"\nMixing naive and aware datetimes raises an error: {error}")

print("\nRule: if your app deals with more than one location or runs on a")
print("server, use timezone-aware datetimes (ZoneInfo) - not naive ones.")