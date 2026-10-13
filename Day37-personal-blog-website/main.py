# Day 37 - Personal Blog Website
# Concept: Routes & Templates
# Goal: Practice using Jinja2 templates instead of returning raw HTML strings from Python

# Requires: pip install flask
# Folder structure needed:
#   Day37-personal-blog-website/
#       main.py
#       templates/
#           index.html
#           post.html
#           about.html

from flask import Flask, render_template

app = Flask(__name__)

# --- Sample blog data (in a real app this would come from a database) ---
blog_posts = [
    {"id": 1, "title": "Learning Python", "content": "Today I started my 100 days of Python journey!", "author": "Kalid"},
    {"id": 2, "title": "Flask Basics", "content": "Flask makes it easy to build web apps with Python.", "author": "Kalid"},
    {"id": 3, "title": "Why Templates Matter", "content": "Templates keep HTML separate from Python logic.", "author": "Kalid"},
]


# --- render_template() looks for files inside the 'templates' folder automatically ---
@app.route("/")
def home():
    # passing data into the template - blog_posts becomes available INSIDE the HTML
    return render_template("index.html", posts=blog_posts, site_name="My Python Blog")


# --- A dynamic route that finds ONE post and renders a different template for it ---
@app.route("/post/<int:post_id>")
def show_post(post_id):
    # find the matching post, or None if it doesn't exist
    post = next((p for p in blog_posts if p["id"] == post_id), None)

    if post is None:
        return render_template("404.html"), 404   # returning a status code alongside the template

    return render_template("post.html", post=post)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
