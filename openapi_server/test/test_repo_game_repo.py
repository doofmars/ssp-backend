import unittest

from unittest.mock import MagicMock

from bson import ObjectId

from openapi_server.models import Game, GameStatus, Player

import mongomock

from openapi_server.repos.game_repo import GameRepo


class TestGameRepo(unittest.TestCase):

    mock_client = None
    game_repo = None

    @classmethod
    def setUpClass(cls):
        cls.mock_client = mongomock.MongoClient()
        cls.game_repo = GameRepo()
        cls.game_repo.games_collection = cls.mock_client.db.collection

    def test_get_game(self):
        mock_game_id = ObjectId("42caffeaffeb401234567890")
        expected_name = "Mock Game"
        mock_game = {"_id": mock_game_id, "host": {"name": expected_name}, "status": "Playing"}

        self.game_repo.games_collection.find_one = MagicMock(return_value=mock_game)

        result = self.game_repo.get_game(mock_game_id)

        self.assertIsInstance(result, Game)
        self.assertEqual(mock_game["_id"], result.id)
        self.assertEqual(expected_name, result.host.name)
        self.assertEqual(mock_game["status"], result.status)

    def test_create_game(self):
        mock_game = Game(host=Player(name="Mock Game"), status=GameStatus.WAITING_FOR_GUEST)
        mock_game_dict = mock_game.to_dict()
        mock_result = MagicMock()
        mock_result.inserted_id = "1234"

        self.game_repo.games_collection.insert_one = MagicMock(return_value=mock_result)

        result = self.game_repo.create_game(mock_game)

        self.assertIsInstance(result, Game)
        self.assertEqual(mock_result.inserted_id, result.id)

    def test_update_game(self):
        mock_game = Game(id="42caffeaffeb401234567890", host=Player(name="foo"), status=GameStatus.RUNNING_FIGHT)
        mock_game_dict = mock_game.to_dict()

        self.game_repo.games_collection.update_one = MagicMock()

        result = self.game_repo.update_game(mock_game)

        self.assertIsInstance(result, Game)
        self.assertEqual(mock_game.id, result.id)

    def test_get_games(self):
        mock_games = [
            {"_id": "1234", "host": {"name": "Mock Game1"}, "status": GameStatus.RUNNING_SAME_WEAPON},
            {"_id": "5678", "host": {"name": "Mock Game2"}, "status": GameStatus.WAITING_FOR_GUEST}
        ]

        self.game_repo.games_collection.find = MagicMock(return_value=mock_games)

        result = self.game_repo.get_games()

        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, Game) for item in result))
        self.assertEqual(len(mock_games), len(result))

    def test_get_games_with_status(self):
        mock_games = [
            {"_id": "5678", "host": {"name": "Mock Game2"}, "status": GameStatus.WAITING_FOR_GUEST}
        ]

        self.game_repo.games_collection.find = MagicMock(return_value=mock_games)

        result = self.game_repo.get_games(GameStatus.WAITING_FOR_GUEST)

        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, Game) for item in result))
        self.assertEqual(1, len(result))


if __name__ == "__main__":
    unittest.main()
