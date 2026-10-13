# Day 38 - Contact Form App
# Concept: Forms & User Input
# Goal: Practice handling HTML forms in Flask - both GET and POST requests

# Requires: pip install flask
# Folder structure needed:
#   Day38-contact-form-app/
#       main.py
#       templates/
#           contact.html
#           success.html

from flask import Flask, render_template, request

app = Flask(__name__)

# --- In-memory storage for submitted messages (a real app would use a database) ---
submitted_messages = []


# --- methods=["GET", "POST"] - this route accepts BOTH request types ---
# GET  - when the user first visits the page (just show the empty form)
# POST - when the user submits the form (process the data)
@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # --- request.form - a dictionary-like object holding submitted form data ---
        # the keys match the "name" attribute of each <input> in the HTML form
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # --- Basic server-side validation ---
        # Never trust that the browser's own validation was enough -
        # always validate again on the server side too.
        errors = []
        if not name:
            errors.append("Name is required.")
        if not email or "@" not in email:
            errors.append("A valid email is required.")
        if not message:
            errors.append("Message is required.")

        if errors:
            # re-render the SAME form, but pass the errors back to show them
            return render_template("contact.html", errors=errors, name=name, email=email, message=message)

        # --- If validation passed, "save" the message and redirect to a success page ---
        submitted_messages.append({"name": name, "email": email, "message": message})
        return render_template("success.html", name=name)

    # --- GET request - just show the empty form ---
    return render_template("contact.html", errors=None, name="", email="", message="")


# --- A route to view all "submitted" messages - simulating an admin view ---
@app.route("/messages")
def view_messages():
    return render_template("messages.html", messages=submitted_messages)


# --- request.args - used for GET-based query parameters, e.g. /search?q=python ---
@app.route("/search")
def search():
    query = request.args.get("q", "")   # default to empty string if not provided
    if query:
        return f"You searched for: {query}"
    return "No search query provided. Try /search?q=python"


if __name__ == "__main__":
    app.run(debug=True)
