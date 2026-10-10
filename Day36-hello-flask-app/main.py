# Day 36 - Hello Flask App
# Concept: Flask Basics
# Goal: Practice creating a minimal web server with Flask

# Requires: pip install flask

from flask import Flask

# --- Creating a Flask application instance ---
# __name__ tells Flask where to look for resources (templates, static files, etc.)
app = Flask(__name__)


# --- A ROUTE - maps a URL path to a Python function ---
# The @app.route() decorator is what connects the URL to the function below it
@app.route("/")
def home():
    return "Hello, Flask! This is my first web app."


# --- Another route, a different URL path ---
@app.route("/about")
def about():
    return "This is the About page. Built on Day 36 of my Python journey."


# --- A route that returns actual HTML instead of plain text ---
@app.route("/welcome")
def welcome():
    return """
    <html>
        <head><title>Welcome</title></head>
        <body>
            <h1>Welcome to my Flask app!</h1>
            <p>This HTML is being returned directly from a Python function.</p>
        </body>
    </html>
    """


# --- A route with a DYNAMIC part in the URL ---
# <name> in the route becomes a parameter passed into the function
@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}! Welcome to Flask."


# --- A dynamic route with a specific data type ---
# <int:age> means Flask will only match this route if age is a valid integer,
# and it automatically converts it to an int for you
@app.route("/age/<int:age>")
def show_age(age):
    next_year = age + 1
    return f"You are {age} years old. Next year you'll be {next_year}."


# --- Multiple dynamic parts in one route ---
@app.route("/user/<username>/post/<int:post_id>")
def show_user_post(username, post_id):
    return f"Showing post #{post_id} by user '{username}'."


# --- Running the app ---
# debug=True enables auto-reload on code changes and shows detailed error pages -
# very useful during development, but should be turned OFF in production.
if __name__ == "__main__":
    app.run(debug=True)

# --- To run this file: ---
#   python main.py
# Then open a browser and visit:
#   http://127.0.0.1:5000/
#   http://127.0.0.1:5000/about
#   http://127.0.0.1:5000/welcome
#   http://127.0.0.1:5000/greet/Kalid
#   http://127.0.0.1:5000/age/30
#   http://127.0.0.1:5000/user/kalid123/post/5