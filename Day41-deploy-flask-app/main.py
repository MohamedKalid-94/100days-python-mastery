# Day 41 - Deploy Flask App
# Concept: Deployment
# Goal: Prepare a Flask app to run on a PRODUCTION server instead of the
#       development server we've used every day so far (app.run(debug=True))

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! This Flask app is set up for production deployment."


@app.route("/health")
def health_check():
    # A "health check" route - many hosting platforms ping this automatically
    # to confirm your app is alive and responding correctly.
    return {"status": "ok"}, 200


# --- IMPORTANT: no app.run(debug=True) call at the bottom of this file ---
# In every previous Flask day, this file was run DIRECTLY with `python main.py`,
# which used Flask's own built-in development server (the one that prints
# the "WARNING: this is a development server" message we saw on Day36).
#
# For real deployment, a separate PRODUCTION WSGI SERVER (like Gunicorn or
# Waitress) imports this file and runs the `app` object itself - it does NOT
# call app.run(). That's why there's no "if __name__ == '__main__':" block
# here anymore; this file's job now is just to DEFINE the app, not run it.
