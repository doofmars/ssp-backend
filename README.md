# ssp-backend
The game backend service for [ssp-online](https://github.com/doofmars/ssp-online) play [here](https://doofmars.github.io/ssp-online/)

Created during for studies course Middleware Technology 

Video for reference: https://www.youtube.com/watch?v=Q2sDtTbzHiI

# Recreate

To recreate the API, run the following command:
```bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/api/api.yaml -g python-flask -o /local/ssp-backend-flask --ignore-file-override /local/ssp-backend-flask/.openapi-generator-ignore
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