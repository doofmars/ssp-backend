import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.create_game import CreateGame  # noqa: E501
from openapi_server.models.game import Game  # noqa: E501
from openapi_server.models.game_status import GameStatus  # noqa: E501
from openapi_server import util


def game_game_id_get(game_id):  # noqa: E501
    """game_game_id_get

    Get information about a game # noqa: E501

    :param game_id: ID of game to return
    :type game_id: str

    :rtype: Union[Game, Tuple[Game, int], Tuple[Game, int, Dict[str, str]]
    """
    return 'do some magic!'


def game_put(create_game):  # noqa: E501
    """game_put

    Create a new game # noqa: E501

    :param create_game: 
    :type create_game: dict | bytes

    :rtype: Union[Game, Tuple[Game, int], Tuple[Game, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_game = CreateGame.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def games_get(status=None):  # noqa: E501
    """games_get

    Get all games # noqa: E501

    :param status: Status of the game
    :type status: dict | bytes

    :rtype: Union[List[Game], Tuple[List[Game], int], Tuple[List[Game], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        status =  GameStatus.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
