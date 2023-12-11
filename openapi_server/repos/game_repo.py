from openapi_server.models import Game


class GameRepo:

    def create(self, game: Game):
        return db.session.add(game)