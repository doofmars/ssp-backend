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

import de.doofmars.ssp.backend.models.Pawn
import de.doofmars.ssp.backend.models.Player
import kotlinx.serialization.Serializable

/**
 * 
 * @param player 
 * @param pawn 
 * @param x 
 * @param y 
 * @param action 
 */
@Serializable
data class GameGameIdTurnPostRequest(
    val player: Player,
    val pawn: Pawn,
    val x: kotlin.Long,
    val y: kotlin.Long,
    val action: GameGameIdTurnPostRequest.Action? = null
) 
{
    /**
    * 
    * Values: MOVE_X_MINUS1,MOVE_X_PLUS1,MOVE_Y_MINUS1,MOVE_Y_PLUS1,PLACE_TRAP,PLACE_FLAG,SHUFFLE_PAWNS
    */
    enum class Action(val value: kotlin.String){
        MOVE_X_MINUS1("MOVE_X-1"),
        MOVE_X_PLUS1("MOVE_X+1"),
        MOVE_Y_MINUS1("MOVE_Y-1"),
        MOVE_Y_PLUS1("MOVE_Y+1"),
        PLACE_TRAP("PLACE_TRAP"),
        PLACE_FLAG("PLACE_FLAG"),
        SHUFFLE_PAWNS("SHUFFLE_PAWNS");
    }
}

