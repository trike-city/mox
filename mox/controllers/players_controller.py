from mox.data import PlayerRepository
from .controller import Controller


class PlayersController(Controller):
    resource = 'players'

    def __init__(self, database):
        self.repo = PlayerRepository(database)

    def create(self, request):
        player = self.repo.create(request.json)
        return self.response(player.serialize(), 201)
