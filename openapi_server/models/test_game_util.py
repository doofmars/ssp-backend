import unittest
from unittest.mock import MagicMock

from openapi_server.models import GameStatus, CreateGame
from openapi_server.models.game_util import create_game_to_game


class TestCreateGameToGame(unittest.TestCase):

    def test_create_game_to_game(self):
        create_game_sample = {
            "host": {
                "name": "test_host",
                "id": 0,
                "key": "key"
            }
        }
        create_game = CreateGame.from_dict(create_game_sample)
        game = create_game_to_game(create_game)

        self.assertEqual(game.host.name, 'test_host')
        self.assertEqual(game.status, GameStatus.WAITING_FOR_GUEST)


if __name__ == "__main__":
    unittest.main()
