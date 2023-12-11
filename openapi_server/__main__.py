import os

from flask import render_template  # Remove: import Flask

import psycopg2
import connexion

app = connexion.FlaskApp(__name__, specification_dir='./openapi/')

app.add_api("openapi.yaml")


@app.route("/")
def home():
    return render_template("index.html")


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database='ssp_db',
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    return conn


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
