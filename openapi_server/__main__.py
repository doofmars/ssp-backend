from .factory import start_server

# This is the entrypoint for the application when running locally as python module (used in docker-compose)
# Usage example: python -m openapi_server from the project root
if __name__ == "__main__":
    start_server()
