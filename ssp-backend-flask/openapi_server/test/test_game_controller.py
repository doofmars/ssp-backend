# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.game import Game  # noqa: E501
from openapi_server.models.game_game_id_turn_post_request import GameGameIdTurnPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGameController(BaseTestCase):
    """GameController integration test stubs"""

    def test_game_game_id_turn_post(self):
        """Test case for game_game_id_turn_post

        
        """
        game_game_id_turn_post_request = openapi_server.GameGameIdTurnPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/game/{game_id}/turn'.format(game_id='game_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(game_game_id_turn_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
