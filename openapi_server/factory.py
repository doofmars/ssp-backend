import os

import connexion
from connexion.middleware import MiddlewarePosition
from flask import render_template
from starlette.middleware.cors import CORSMiddleware


def start_server():
    app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
    app.add_api("openapi.yaml")

    print("Running in FLASK_ENV: " + str(os.environ.get("FLASK_ENV")))

    if os.environ.get("FLASK_ENV") == "development":
        app.add_middleware(
            CORSMiddleware,
            position=MiddlewarePosition.BEFORE_EXCEPTION,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

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
