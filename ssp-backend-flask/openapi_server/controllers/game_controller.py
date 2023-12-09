import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.game import Game  # noqa: E501
from openapi_server.models.game_game_id_turn_post_request import GameGameIdTurnPostRequest  # noqa: E501
from openapi_server import util


def game_game_id_turn_post(game_id, game_game_id_turn_post_request):  # noqa: E501
    """game_game_id_turn_post

    Do a turn # noqa: E501

    :param game_id: ID of game to return
    :type game_id: str
    :param game_game_id_turn_post_request: 
    :type game_game_id_turn_post_request: dict | bytes

    :rtype: Union[Game, Tuple[Game, int], Tuple[Game, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        game_game_id_turn_post_request = GameGameIdTurnPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
