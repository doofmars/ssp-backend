import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.create_game import CreateGame
from openapi_server.models.game import Game
from openapi_server.models.game_status import GameStatus
from openapi_server import util
from openapi_server.models.game_util import create_game_to_game
from openapi_server.repos.game_repo import GameRepo

game_repo = GameRepo()


def game_game_id_get(game_id):
    """game_game_id_get

    Get information about a game

    :param game_id: ID of game to return
    :type game_id: str

    :rtype: Union[Game, Tuple[Game, int], Tuple[Game, int, Dict[str, str]]
    """
    game = game_repo.get_game(game_id)
    if game is None:
        return None, 404
    return game.to_dict(), 200


def game_put(create_game: CreateGame):
    """game_put

    Create a new game

    :param create_game:
    :type create_game: dict | bytes

    :rtype: Union[Game, Tuple[Game, int], Tuple[Game, int, Dict[str, str]]
    """
    # Serialize the CreateGame object into a Game object and set the required fields to their default values
    game = create_game_to_game(create_game)
    game = game_repo.create_game(game)
    return game.to_dict(), 201


def games_get(status: GameStatus = None):
    """games_get

    Get all games

    :param status: Status of the game
    :type status: dict | bytes

    :rtype: Union[List[Game], Tuple[List[Game], int], Tuple[List[Game], int, Dict[str, str]]
    """
    games = game_repo.get_games(status)
    return [game.to_dict() for game in games], 200


def game_game_id_delete(game_id):
    """game_game_id_delete

    Delete a game

    :param game_id: ID of game to delete
    :type game_id: str

    :rtype: Union[Game, Tuple[Game, int], Tuple[Game, int, Dict[str, str]]
    """
    game = game_repo.get_game(game_id)
    if game is None:
        return None, 404
    game_repo.delete_game(game_id)
    return None, 200
