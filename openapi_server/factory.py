import os

import connexion
from flask import render_template


def start_server():
    app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
    app.add_api("openapi.yaml")

    # Check for required environment variable DB_USERNAME DB_PASSWORD and DB_HOST and fail to start if not set
    if not os.environ.get("DB_USERNAME"):
        print("DB_USERNAME environment variable not set")
        exit(1)
    if not os.environ.get("DB_PASSWORD"):
        print("DB_PASSWORD environment variable not set")
        exit(1)
    if not os.environ.get("DB_HOST"):
        print("DB_HOST environment variable not set")
        exit(1)

    @app.route("/")
    def home():
        return render_template("index.html")

    app.run(host="0.0.0.0", port=8080)
