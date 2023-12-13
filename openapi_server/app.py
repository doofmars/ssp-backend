import os

from flask import render_template  # Remove: import Flask

import psycopg2
import connexion

from openapi_server.init_db import init_db

app = connexion.FlaskApp(__name__, specification_dir='./openapi/')

app.add_api("openapi.yaml")


@app.route("/")
def home():
    return render_template("index.html")


init_db()
app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
