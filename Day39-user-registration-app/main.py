# Day 39 - User Registration App
# Concept: Database Integration
# Goal: Practice connecting Flask to a real database (SQLite) instead of
#       storing data only in memory (which disappears when the app restarts)

# Requires: pip install flask
# sqlite3 is BUILT INTO Python - no extra install needed for the database itself.
#
# Folder structure needed:
#   Day39-user-registration-app/
#       main.py
#       templates/
#           register.html
#           users.html

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE_NAME = "users.db"


# --- A function to set up the database and table if they don't exist yet ---
def init_db():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # CREATE TABLE IF NOT EXISTS - safe to run every time the app starts,
    # won't wipe existing data or error if the table already exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()   # commit() saves the changes to the database file
    connection.close()    # always close the connection when done


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        errors = []
        if not username:
            errors.append("Username is required.")
        if not email or "@" not in email:
            errors.append("A valid email is required.")
        if not password or len(password) < 6:
            errors.append("Password must be at least 6 characters.")

        if errors:
            return render_template("register.html", errors=errors, username=username, email=email)

        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        try:
            # --- Using ? placeholders - NEVER insert user input directly into SQL strings ---
            # This is critical for security: directly formatting user input into SQL
            # (e.g. f"INSERT INTO users VALUES ('{username}')") opens the door to
            # SQL injection attacks. Placeholders let sqlite3 handle escaping safely.
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)
            )
            connection.commit()
        except sqlite3.IntegrityError:
            # this fires if the UNIQUE constraint on username is violated
            connection.close()
            return render_template("register.html", errors=["That username is already taken."], username=username, email=email)

        connection.close()

        # --- redirect() sends the browser to a different route after success ---
        # This follows the "Post/Redirect/Get" pattern - prevents the browser from
        # re-submitting the form if the user refreshes the success page.
        return redirect(url_for("view_users"))

    return render_template("register.html", errors=None, username="", email="")


@app.route("/users")
def view_users():
    connection = sqlite3.connect(DATABASE_NAME)
    # row_factory lets us access columns by NAME instead of just position
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # SELECT - never fetch the password column in a real app; shown minimally here
    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()   # fetchall() gets ALL matching rows as a list

    connection.close()

    return render_template("users.html", users=users)


@app.route("/user/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    connection.commit()
    connection.close()

    return redirect(url_for("view_users"))


if __name__ == "__main__":
    init_db()   # make sure the table exists before the app starts handling requests
    app.run(debug=True)
