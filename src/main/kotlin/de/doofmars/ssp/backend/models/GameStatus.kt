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
package de.doofmars.ssp.backend.models


/**
* 
* Values: WAITING_FOR_GUEST,SETUP_PLACE_FLAG,SETUP_PLACE_TRAP,SETUP_SHUFFLE_PAWNS,RUNNING_PLAYER_TURN,RUNNING_OPPONENT_TURN,RUNNING_FIGHT,RUNNING_SAME_WEAPON,FINISHED_HOST_WIN,FINISHED_GUEST_WIN,FINISHED_DRAW
*/
enum class GameStatus(val value: kotlin.String) {

    WAITING_FOR_GUEST("WAITING_FOR_GUEST"),

    SETUP_PLACE_FLAG("SETUP_PLACE_FLAG"),

    SETUP_PLACE_TRAP("SETUP_PLACE_TRAP"),

    SETUP_SHUFFLE_PAWNS("SETUP_SHUFFLE_PAWNS"),

    RUNNING_PLAYER_TURN("RUNNING_PLAYER_TURN"),

    RUNNING_OPPONENT_TURN("RUNNING_OPPONENT_TURN"),

    RUNNING_FIGHT("RUNNING_FIGHT"),

    RUNNING_SAME_WEAPON("RUNNING_SAME_WEAPON"),

    FINISHED_HOST_WIN("FINISHED_HOST_WIN"),

    FINISHED_GUEST_WIN("FINISHED_GUEST_WIN"),

    FINISHED_DRAW("FINISHED_DRAW");

}

