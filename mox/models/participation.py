class Participation:
    def __init__(self, id, tournament_id, player_id):
        self.id = id
        self.tournament_id = tournament_id
        self.player_id = player_id

    @staticmethod
    def build(attributes):
        return Participation(
            id=attributes['id'],
            tournament_id=attributes['tournament_id'],
            player_id=attributes['player_id']
        )
