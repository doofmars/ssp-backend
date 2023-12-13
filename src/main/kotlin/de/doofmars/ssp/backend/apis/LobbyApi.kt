/**
* SSP-Online Backend
* This is a the backend for the SSP Online Game. It is a RESTful API that is used by the frontend to play the game.  Some useful links: - [ssp-online](https://github.com/doofmars/ssp-online) - The source code for the SSP Online Game - [ssp-backend](https://github.com/doofmars/ssp-backend) - The source code for the SSP Backend
*
* The version of the OpenAPI document: 1.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package de.doofmars.ssp.backend.apis

import com.google.gson.Gson
import io.ktor.server.application.*
import io.ktor.server.response.*
import de.doofmars.ssp.backend.Paths
import io.ktor.server.resources.get
import io.ktor.server.resources.put
import io.ktor.server.routing.*

fun Route.lobbyApi() {
    val gson = Gson()
    val empty = mutableMapOf<String, Any?>()

    get<Paths.GameGameIdGet> {
        val exampleContentType = "application/json"
        val exampleContentString = """{
          "currentRound" : 5,
          "winner" : "NONE",
          "last_update" : "2000-01-23T04:56:07.000+00:00",
          "host" : {
            "name" : "name",
            "id" : 0,
            "key" : "key"
          },
          "guest" : {
            "name" : "name",
            "id" : 0,
            "key" : "key"
          },
          "id" : "id",
          "board" : {
            "grid" : [ [ {
              "owner" : "HOST",
              "item" : "ROCK"
            }, {
              "owner" : "HOST",
              "item" : "ROCK"
            } ], [ {
              "owner" : "HOST",
              "item" : "ROCK"
            }, {
              "owner" : "HOST",
              "item" : "ROCK"
            } ] ],
            "width" : 6,
            "height" : 1
          }
        }"""
        
        when (exampleContentType) {
            "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
            else -> call.respondText(exampleContentString)
        }
        
    }

    put<Paths.GamePut> {
        val exampleContentType = "application/json"
        val exampleContentString = """{
          "currentRound" : 5,
          "winner" : "NONE",
          "last_update" : "2000-01-23T04:56:07.000+00:00",
          "host" : {
            "name" : "name",
            "id" : 0,
            "key" : "key"
          },
          "guest" : {
            "name" : "name",
            "id" : 0,
            "key" : "key"
          },
          "id" : "id",
          "board" : {
            "grid" : [ [ {
              "owner" : "HOST",
              "item" : "ROCK"
            }, {
              "owner" : "HOST",
              "item" : "ROCK"
            } ], [ {
              "owner" : "HOST",
              "item" : "ROCK"
            }, {
              "owner" : "HOST",
              "item" : "ROCK"
            } ] ],
            "width" : 6,
            "height" : 1
          }
        }"""
        
        when (exampleContentType) {
            "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
            else -> call.respondText(exampleContentString)
        }
        
    }

    get<Paths.GamesGet> {
        val exampleContentType = "application/json"
        val exampleContentString = """[ {
          "currentRound" : 5,
          "winner" : "NONE",
          "last_update" : "2000-01-23T04:56:07.000+00:00",
          "host" : {
            "name" : "name",
            "id" : 0,
            "key" : "key"
          },
          "guest" : {
            "name" : "name",
            "id" : 0,
            "key" : "key"
          },
          "id" : "id",
          "board" : {
            "grid" : [ [ {
              "owner" : "HOST",
              "item" : "ROCK"
            }, {
              "owner" : "HOST",
              "item" : "ROCK"
            } ], [ {
              "owner" : "HOST",
              "item" : "ROCK"
            }, {
              "owner" : "HOST",
              "item" : "ROCK"
            } ] ],
            "width" : 6,
            "height" : 1
          }
        }, {
          "currentRound" : 5,
          "winner" : "NONE",
          "last_update" : "2000-01-23T04:56:07.000+00:00",
          "host" : {
            "name" : "name",
            "id" : 0,
            "key" : "key"
          },
          "guest" : {
            "name" : "name",
            "id" : 0,
            "key" : "key"
          },
          "id" : "id",
          "board" : {
            "grid" : [ [ {
              "owner" : "HOST",
              "item" : "ROCK"
            }, {
              "owner" : "HOST",
              "item" : "ROCK"
            } ], [ {
              "owner" : "HOST",
              "item" : "ROCK"
            }, {
              "owner" : "HOST",
              "item" : "ROCK"
            } ] ],
            "width" : 6,
            "height" : 1
          }
        } ]"""
        
        when (exampleContentType) {
            "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
            else -> call.respondText(exampleContentString)
        }
        
    }

}
