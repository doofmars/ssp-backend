# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_game import CreateGame  # noqa: E501
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.game_status import GameStatus  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLobbyController(BaseTestCase):
    """LobbyController integration test stubs"""

    def test_game_game_id_get(self):
        """Test case for game_game_id_get

        
        """
        response = self.client.open(
            '/game/{gameId}'.format(game_id=Id()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_game_put(self):
        """Test case for game_put

        
        """
        body = CreateGame()
        response = self.client.open(
            '/game',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_games_get(self):
        """Test case for games_get

        
        """
        query_string = [('status', GameStatus())]
        response = self.client.open(
            '/games',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
