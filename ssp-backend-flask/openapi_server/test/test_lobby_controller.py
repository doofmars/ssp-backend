import unittest

from flask import json

from openapi_server.models.create_game import CreateGame  # noqa: E501
from openapi_server.models.game import Game  # noqa: E501
from openapi_server.models.game_status import GameStatus  # noqa: E501
from openapi_server.test import BaseTestCase


class TestLobbyController(BaseTestCase):
    """LobbyController integration test stubs"""

    def test_game_game_id_get(self):
        """Test case for game_game_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/game/{game_id}'.format(game_id='game_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_game_put(self):
        """Test case for game_put

        
        """
        create_game = {"host":{"name":"name","id":0,"key":"key"}}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/game',
            method='PUT',
            headers=headers,
            data=json.dumps(create_game),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_games_get(self):
        """Test case for games_get

        
        """
        query_string = [('status', openapi_server.GameStatus())]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/games',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
