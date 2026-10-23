# Day 41 - Deploy Flask App

## Why this day is different from Day36-40

Every previous Flask day ran with:

    python main.py

which starts Flask's own **development server** (the one that prints the
"WARNING: this is a development server" message). That server is fine for
learning and local testing, but it is not built to handle real traffic,
multiple users, or production security concerns.

This day switches to a **production WSGI server** instead: Gunicorn.

## What changed in main.py

- No `app.run(debug=True)` call, and no `if __name__ == "__main__":` block.
- The file's only job now is to create and configure the `app` object.
  A production server imports this file and runs `app` itself.
- Added a `/health` route - many hosting platforms (Render, Railway,
  Heroku-style platforms) automatically ping a health check URL to confirm
  the app is alive after deployment.

## Running it locally with Gunicorn (Mac/Linux, or WSL on Windows)

Gunicorn does not run natively on Windows. If you're on Windows, either use
WSL, or use **Waitress** instead (see below).

    pip install -r requirements.txt
    gunicorn main:app

This starts the app using a real production server instead of Flask's
built-in one. Visit http://127.0.0.1:8000/ to see it running.

## Running it locally with Waitress (Windows-friendly alternative)

    pip install flask waitress

Then create a small run script:

    from waitress import serve
    from main import app

    if __name__ == "__main__":
        serve(app, host="0.0.0.0", port=8000)

Run it with `python run_waitress.py`. Same idea as Gunicorn - a real
production server, just one that works natively on Windows too.

## The Procfile

The `Procfile` in this folder tells hosting platforms (Render, Railway,
Heroku, etc.) how to start your app in production:

    web: gunicorn main:app

Most platforms detect this automatically once you push your repo to them.

## Deploying for real (high-level steps)

1. Push this folder to GitHub (as part of your 100-days repo).
2. Sign up for a hosting platform that supports Python/Flask - Render and
   Railway both have free tiers and are commonly used for small projects.
3. Connect your GitHub repo to the platform.
4. Point it at this folder, and it should detect `requirements.txt` and
   the `Procfile` automatically.
5. The platform installs dependencies and runs `gunicorn main:app` for you.
6. You get a public URL where the app is live.

## Key takeaway

Development server (`app.run(debug=True)`) = for YOU, while building and
testing locally.

Production WSGI server (Gunicorn/Waitress) = for REAL USERS, once you
actually deploy the app somewhere.
