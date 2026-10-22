# Day 40 - Mini Weather API
# Concept: REST APIs
# Goal: Practice BUILDING a REST API with Flask (Day19 was about CONSUMING one -
#       this day flips it around: now we're the ones providing the data)

# Requires: pip install flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# --- In-memory "database" of weather data (a real API would use an actual database) ---
weather_data = {
    "Bengaluru": {"temperature_C": 26, "condition": "Cloudy", "humidity": 65},
    "Mumbai": {"temperature_C": 31, "condition": "Sunny", "humidity": 78},
    "Delhi": {"temperature_C": 34, "condition": "Hazy", "humidity": 40},
}


# --- A REST API returns JSON, not HTML - jsonify() converts a Python dict/list into JSON ---
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Mini Weather API",
        "endpoints": ["/weather", "/weather/<city>", "/weather (POST)"]
    })


# --- GET /weather - return ALL cities' weather data ---
@app.route("/weather", methods=["GET"])
def get_all_weather():
    return jsonify(weather_data)


# --- GET /weather/<city> - return weather for ONE specific city ---
@app.route("/weather/<city>", methods=["GET"])
def get_city_weather(city):
    # .get() with a case-insensitive-ish match by title-casing the input
    city_data = weather_data.get(city.title())

    if city_data is None:
        # --- Returning a proper HTTP status code alongside the JSON ---
        # 404 = Not Found - REST APIs should always return meaningful status codes,
        # not just 200 for everything
        return jsonify({"error": f"No weather data found for '{city}'"}), 404

    return jsonify({"city": city.title(), **city_data})


# --- POST /weather - ADD a new city's weather data ---
@app.route("/weather", methods=["POST"])
def add_city_weather():
    # --- request.get_json() reads JSON data sent in the request body ---
    # (different from request.form, which reads regular HTML form data)
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400   # 400 = Bad Request

    city = data.get("city")
    temperature = data.get("temperature_C")
    condition = data.get("condition")
    humidity = data.get("humidity")

    if not all([city, temperature is not None, condition, humidity is not None]):
        return jsonify({"error": "Missing required fields: city, temperature_C, condition, humidity"}), 400

    weather_data[city.title()] = {
        "temperature_C": temperature,
        "condition": condition,
        "humidity": humidity,
    }

    # --- 201 = Created - the correct status code for a successful POST that creates something ---
    return jsonify({"message": f"Weather data added for {city.title()}", "data": weather_data[city.title()]}), 201


# --- PUT /weather/<city> - UPDATE an existing city's weather data ---
@app.route("/weather/<city>", methods=["PUT"])
def update_city_weather(city):
    if city.title() not in weather_data:
        return jsonify({"error": f"'{city}' not found. Use POST to add it first."}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # only update fields that were actually provided
    weather_data[city.title()].update(data)

    return jsonify({"message": f"Weather data updated for {city.title()}", "data": weather_data[city.title()]})


# --- DELETE /weather/<city> - REMOVE a city's weather data ---
@app.route("/weather/<city>", methods=["DELETE"])
def delete_city_weather(city):
    if city.title() not in weather_data:
        return jsonify({"error": f"'{city}' not found."}), 404

    del weather_data[city.title()]
    return jsonify({"message": f"Weather data for {city.title()} deleted."})


# --- A custom 404 handler for the WHOLE app - fires for any unmatched route ---
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

# --- To test this API, you can use a browser for GET requests, or a tool like ---
# --- curl / Postman / the requests library for POST, PUT, and DELETE. Examples: ---
#
# GET all:      curl http://127.0.0.1:5000/weather
# GET one:      curl http://127.0.0.1:5000/weather/Mumbai
# POST new:     curl -X POST http://127.0.0.1:5000/weather -H "Content-Type: application/json" -d "{\"city\":\"Chennai\",\"temperature_C\":30,\"condition\":\"Humid\",\"humidity\":80}"
# PUT update:   curl -X PUT http://127.0.0.1:5000/weather/Chennai -H "Content-Type: application/json" -d "{\"temperature_C\":32}"
# DELETE:       curl -X DELETE http://127.0.0.1:5000/weather/Chennai