import pymongo
from bson import ObjectId

from openapi_server.models import Game, GameStatus


class GameRepo:
    def __init__(self):
        mongo_client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
        db = mongo_client["ssp_db"]
        self.games_collection = db["games"]

    def get_game(self, game_id):
        """
        :param game_id: The id of the game in the database.
        :return: The game object with the matching id, or None if no matching game was found.
        """
        game_dict = self.games_collection.find_one({"_id": ObjectId(game_id)})
        if game_dict is None:
            return None
        game = Game.from_dict(game_dict)
        game.id = game_dict["_id"]
        return game

    def create_game(self, game: Game) -> Game:
        """
        :param game: A Game object representing the game to be created and inserted into the collection.
        :return: The Game object with the updated id value after insertion into the collection.

        The `create_game` method takes a Game object as a parameter and inserts it into the games_collection.
        The method returns the Game object with the updated id value after insertion. Before
        * inserting the game, the method removes the id field from the game_dict, as it might cause duplicate key errors.
        The inserted id is then assigned to the game.id attribute.

        Example Usage:
        ```python
        game = Game(...)
        new_game = create_game(game)
        ```
        """
        game_dict = game.to_dict()
        # remove id from dict, otherwise we might get a duplicate key
        game_dict.pop("id", None)
        result = self.games_collection.insert_one(game_dict)
        game.id = str(result.inserted_id)
        return game

    def update_game(self, game: Game) -> Game:
        game_dict = game.to_dict()
        # remove id from dict, otherwise we might get a duplicate key
        game_dict.pop("id", None)
        self.games_collection.update_one({"_id": game.id}, {"$set": game_dict})
        return game

    def get_games(self, status: GameStatus = None) -> [Game]:
        if status is None:
            game_dicts = self.games_collection.find()
        else:
            game_dicts = self.games_collection.find({"status": str(status)})
        return [Game.from_dict(game_dict) for game_dict in game_dicts]
