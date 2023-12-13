from flask import render_template  # Remove: import Flask

import connexion


app = connexion.FlaskApp(__name__, specification_dir='./openapi/')

app.add_api("openapi.yaml")


@app.route("/")
def home():
    return render_template("index.html")


app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
