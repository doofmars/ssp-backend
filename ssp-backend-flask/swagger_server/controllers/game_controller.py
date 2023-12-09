import connexion
import six

from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.game_id_turn_body import GameIdTurnBody  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server import util


def game_game_id_turn_post(body, game_id):  # noqa: E501
    """game_game_id_turn_post

    Do a turn # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param game_id: ID of game to return
    :type game_id: dict | bytes

    :rtype: Game
    """
    if connexion.request.is_json:
        body = GameIdTurnBody.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        game_id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
