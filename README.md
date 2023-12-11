# de.doofmars.ssp-backend - Kotlin Server library for SSP-Online Backend

The game backend service for [ssp-online](https://github.com/doofmars/ssp-online) play [here](https://doofmars.github.io/ssp-online/)

This is the backend for the SSP Online Game. It is a RESTful API that is used by the frontend to play the game.
Created during for studies course Middleware Technology

Some useful links:
- [ssp-online](https://github.com/doofmars/ssp-online) - The source code for the SSP Online Game
- [ssp-backend](https://github.com/doofmars/ssp-backend) - The source code for the SSP Backend
- Video for reference: https://www.youtube.com/watch?v=Q2sDtTbzHiI
Generated by OpenAPI Generator 7.2.0-SNAPSHOT.

## Recreate

To recreate models or API, run the following command:
```bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
  -i /local/api/openapi.yml \
  --ignore-file-override /local/.openapi-generator-ignore \
  -g kotlin-server \
  -o /local \
  -c /local/api/config.yml
```

## Requires

* Kotlin 1.7.20
* Gradle 7.4.2

## Build

First, create the gradle wrapper script:

```
gradle wrapper
```

Then, run:

```
./gradlew check assemble
```

This runs all tests and packages the library.

## Running

The server builds as a fat jar with a main entrypoint. To start the service, run `java -jar ./build/libs/ssp-backend.jar`.

You may also run in docker:

```
docker build -t ssp-backend .
docker run -p 8080:8080 ssp-backend
```

## Features/Implementation Notes

* Supports JSON inputs/outputs, File inputs, and Form inputs (see ktor documentation for more info).
* ~Supports collection formats for query parameters: csv, tsv, ssv, pipes.~
* Some Kotlin and Java types are fully qualified to avoid conflicts with types defined in OpenAPI definitions.

<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GameApi* | [**gameGameIdTurnPost**](docs/GameApi.md#gamegameidturnpost) | **POST** /game/{gameId}/turn | 
*LobbyApi* | [**gameGameIdGet**](docs/LobbyApi.md#gamegameidget) | **GET** /game/{gameId} | 
*LobbyApi* | [**gamePut**](docs/LobbyApi.md#gameput) | **PUT** /game | 
*LobbyApi* | [**gamesGet**](docs/LobbyApi.md#gamesget) | **GET** /games | 


<a id="documentation-for-models"></a>
## Documentation for Models

 - [de.doofmars.ssp-backend.models.Board](docs/Board.md)
 - [de.doofmars.ssp-backend.models.CreateGame](docs/CreateGame.md)
 - [de.doofmars.ssp-backend.models.Game](docs/Game.md)
 - [de.doofmars.ssp-backend.models.GameGameIdTurnPostRequest](docs/GameGameIdTurnPostRequest.md)
 - [de.doofmars.ssp-backend.models.GameStatus](docs/GameStatus.md)
 - [de.doofmars.ssp-backend.models.Pawn](docs/Pawn.md)
 - [de.doofmars.ssp-backend.models.Player](docs/Player.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.

