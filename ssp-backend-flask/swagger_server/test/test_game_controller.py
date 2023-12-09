# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.game_id_turn_body import GameIdTurnBody  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGameController(BaseTestCase):
    """GameController integration test stubs"""

    def test_game_game_id_turn_post(self):
        """Test case for game_game_id_turn_post

        
        """
        body = GameIdTurnBody()
        response = self.client.open(
            '/game/{gameId}/turn'.format(game_id=Id()),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
