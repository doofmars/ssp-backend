# ssp-backend
The game backend service for [ssp-online](https://github.com/doofmars/ssp-online) play [here](https://doofmars.github.io/ssp-online/)

Created during for studies course Middleware Technology

Video for reference: https://www.youtube.com/watch?v=Q2sDtTbzHiI

# Recreate

To recreate models or API, run the following command:

For the backend server:
```bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
  -i /local/openapi_server/openapi/openapi.yaml \
  -g python-flask \
  -o /local \
  --ignore-file-override /local/.openapi-generator-ignore
```

For the frontend axios client:
```bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
  -i /local/openapi_server/openapi/openapi.yaml \
  -g typescript-axios \
  -o /local/admin-frontend/src/api-client \
  --ignore-file-override /local/admin-frontend/api-client/.openapi-generator-ignore
```

# Local development

To run the server locally, you need to have a local database running. The easiest way to do this is to use docker-compose:
```bash
docker-compose -f dev-docker-compose.yml up -d
```

The following environment variables are required to run the backend locally:
```
DB_HOST=localhost;DB_USERNAME=root;DB_PASSWORD=example
```

## Overview
This server was generated by the [OpenAPI Generator](https://openapi-generator.tech) project. By using the
[OpenAPI-Spec](https://openapis.org) from a remote server, you can easily generate a server stub.  This
is an example of building a OpenAPI-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.9+

## Usage
To run the server, please execute the following from the root directory:

```
pip install -r requirements.txt
python -m openapi_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:8080/openapi.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t openapi_server .

# starting up a container
docker run -p 8080:8080 openapi_server
```

## Running with Docker Compose

To build and run the server, frontend, database and reverse proxy as Docker containers using Docker Compose,
execute the following from the root directory:

```bash
docker-compose up -d
```

## Environment variables
The following environment variables are required to run the server:

| Name          | Description               | Default |
|---------------|---------------------------|---------|
| `DB_HOST`     | Hostname of the database  |         |
| `DB_USERNAME` | Username for the database |         |
| `DB_PASSWORD` | Password for the database |         |
| `DB_PORT`     | Port of the database      | `27017` |
