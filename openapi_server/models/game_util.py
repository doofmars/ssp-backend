from openapi_server.models import CreateGame, Game, GameStatus


def create_game_to_game(create_game: CreateGame) -> Game:
    """Convert a CreateGame object to a Game object

    :param create_game: CreateGame object to convert
    :type create_game: CreateGame
    :return: Game object
    :rtype: Game
    """
    create_game = CreateGame.from_dict(create_game)
    game = Game()
    game.host = create_game.host
    game.status = GameStatus.WAITING_FOR_GUEST
    # Serialize and deserialize the Game object to invoke the required field checks
    return Game.from_dict(game.to_dict())
