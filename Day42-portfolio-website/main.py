# Day 42 - Portfolio Website
# Concept: Flask Capstone
# Goal: Bring together everything from Day36-41 - routes, templates, forms,
#       and static files (CSS) - into one complete portfolio site

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Portfolio data (a real app might load this from a database, like Day39) ---
projects = [
    {
        "id": 1,
        "title": "100 Days of Python",
        "description": "A collection of 100 small Python projects covering fundamentals through Flask.",
        "tech": "Python, Flask, SQLite",
    },
    {
        "id": 2,
        "title": "Mini Weather API",
        "description": "A REST API built with Flask supporting full CRUD operations.",
        "tech": "Python, Flask, REST",
    },
    {
        "id": 3,
        "title": "Expense Tracker GUI",
        "description": "A desktop expense tracker built with Tkinter.",
        "tech": "Python, Tkinter",
    },
]

# --- In-memory storage for contact form submissions (from the Day38 pattern) ---
messages = []


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)

    if project is None:
        return render_template("404.html"), 404

    return render_template("project_detail.html", project=project)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        errors = []
        if not name:
            errors.append("Name is required.")
        if not email or "@" not in email:
            errors.append("A valid email is required.")
        if not message:
            errors.append("Message is required.")

        if errors:
            return render_template("contact.html", errors=errors, name=name, email=email, message=message)

        messages.append({"name": name, "email": email, "message": message})

        # Post/Redirect/Get pattern (from Day39) - avoids duplicate submissions on refresh
        return redirect(url_for("contact_success"))

    return render_template("contact.html", errors=None, name="", email="", message="")


@app.route("/contact/success")
def contact_success():
    return render_template("contact_success.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
