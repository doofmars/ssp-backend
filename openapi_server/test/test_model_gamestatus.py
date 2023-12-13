import unittest

from openapi_server.models import GameStatus


class GameStatusTest(unittest.TestCase):

    def setUp(self):
        # This method will be used to setup your test variables
        self.game_status = GameStatus()  # self.game_status will be a test instance of the GameStatus class

    def tearDown(self):
        # This method will be called after every test and is used to clean up any setup you made
        pass

    def test_from_dict(self):
        # We create a dummy dict to test our function
        dict_data = {}  # We'll use an initial empty dict to check basic functionality

        # We expect that a new instance is created when we call the `from_dict` function
        new_game_status = GameStatus.from_dict(dict_data)

        # We'll check that the game status created is indeed an instance of GameStatus
        self.assertNotIsInstance(new_game_status, GameStatus, "new_game_status is not an instance of GameStatus")

        # Further tests could be added here to check that all the properties are being correctly set
        test = str(GameStatus.FINISHED_DRAW)
        print(test)


if __name__ == '__main__':
    unittest.main()
