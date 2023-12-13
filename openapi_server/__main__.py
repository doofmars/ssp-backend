import connexion

if __name__ == "__main__":
    app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
    app.add_api("openapi.yaml")
    app.run(host="0.0.0.0", port=8080)
