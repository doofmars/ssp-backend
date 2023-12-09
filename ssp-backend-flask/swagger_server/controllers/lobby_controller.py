import connexion
import six

from swagger_server.models.create_game import CreateGame  # noqa: E501
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.game_status import GameStatus  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server import util


def game_game_id_get(game_id):  # noqa: E501
    """game_game_id_get

    Get information about a game # noqa: E501

    :param game_id: ID of game to return
    :type game_id: dict | bytes

    :rtype: Game
    """
    if connexion.request.is_json:
        game_id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def game_put(body):  # noqa: E501
    """game_put

    Create a new game # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Game
    """
    if connexion.request.is_json:
        body = CreateGame.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def games_get(status=None):  # noqa: E501
    """games_get

    Get all games # noqa: E501

    :param status: Status of the game
    :type status: dict | bytes

    :rtype: List[Game]
    """
    if connexion.request.is_json:
        status = GameStatus.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
