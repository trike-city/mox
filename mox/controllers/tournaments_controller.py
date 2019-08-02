from mox.models import Tournament
from .controller import Controller


class TournamentsController(Controller):
    def __init__(self, database):
        self.database = database

    def create(self, request):
        tournament = Tournament.create(request.json)
        return self.response(tournament.serialize(), 201)
