from mox.models import Player
from .controller import Controller


class PlayersController(Controller):
    resource = 'players'

    def __init__(self, database):
        self.database = database

    def create(self, request):
        player = Player.create(request.json)
        return self.response(player.serialize(), 201)
