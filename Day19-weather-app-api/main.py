# Day 19 - Weather App using API
# Concept: APIs (Basics)
# Goal: Practice making HTTP requests to a real API and working with the JSON response

import requests   # third-party library - install with: pip install requests

# --- What is an API? ---
# An API (Application Programming Interface) lets your program request
# data from another service over the internet. You send a request to a
# URL, and the service sends back a response - usually in JSON format.

# --- Making a basic GET request ---
# wttr.in is a free weather service that doesn't require an API key,
# which makes it easy to practice with.
city = "Bengaluru"
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

# --- Checking the response status code ---
# 200 means success. Other common codes: 404 (not found), 500 (server error)
print("Status code:", response.status_code)

if response.status_code == 200:
    print("Request successful!")
else:
    print("Something went wrong with the request.")

# --- Converting the JSON response into a Python dictionary ---
data = response.json()
print("\nType of data:", type(data))

# --- The response is a nested dictionary - explore it like any Python dict ---
current_condition = data["current_condition"][0]

temperature = current_condition["temp_C"]
feels_like = current_condition["FeelsLikeC"]
description = current_condition["weatherDesc"][0]["value"]
humidity = current_condition["humidity"]

print(f"\n--- Weather in {city} ---")
print(f"Temperature: {temperature}°C")
print(f"Feels like: {feels_like}°C")
print(f"Condition: {description}")
print(f"Humidity: {humidity}%")

# --- Passing parameters to an API using the params= argument ---
# This is the standard way to add query parameters, instead of
# manually building the URL string with ?key=value&key2=value2
params = {"format": "j1"}
response2 = requests.get(f"https://wttr.in/{city}", params=params)
print("\nURL built with params=:", response2.url)

# --- Handling errors: what if the request fails? ---
try:
    bad_response = requests.get("https://wttr.in/ThisCityDoesNotExist123", timeout=5)
    bad_response.raise_for_status()   # raises an error if status code is 4xx or 5xx
    print("This won't print if the request failed.")
except requests.exceptions.RequestException as error:
    print(f"\nAPI request failed: {error}")

# --- Using a timeout to avoid waiting forever on a slow/unresponsive API ---
response3 = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
print("\nRequest with timeout succeeded:", response3.status_code == 200)


# ============================================================
# A reusable weather-fetching function
# ============================================================
def get_weather(city_name):
    url = f"https://wttr.in/{city_name}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        return f"Could not fetch weather: {error}"

    data = response.json()
    current = data["current_condition"][0]

    return {
        "city": city_name,
        "temperature_C": current["temp_C"],
        "feels_like_C": current["FeelsLikeC"],
        "condition": current["weatherDesc"][0]["value"],
        "humidity": current["humidity"],
    }


# --- Using the function ---
weather = get_weather("Mumbai")
print("\n--- Using get_weather() function ---")
print(weather)


# ============================================================
# Interactive part: check the weather for any city
# ============================================================
print("\n--- Check the weather ---")
user_city = input("Enter a city name: ")
result = get_weather(user_city)

if isinstance(result, dict):
    print(f"\nWeather in {result['city']}:")
    print(f"Temperature: {result['temperature_C']}°C (feels like {result['feels_like_C']}°C)")
    print(f"Condition: {result['condition']}")
    print(f"Humidity: {result['humidity']}%")
else:
    print(result)   # error message