from mox.models import Participation


class ParticipationRepository:
    __TABLE_NAME = 'participations'

    def __init__(self, database):
        self.database = database

    def create_many(self, tournament, players):
        sql = f'INSERT INTO {self.__TABLE_NAME} (tournament_id, player_id) VALUES (%s, %s) RETURNING *;'
        values = [(tournament.id, p.id,) for p in players]
        self.database.execute(sql, values)
        result = self.database.execute(f'SELECT * FROM {self.__TABLE_NAME} WHERE tournament_id = %s;', (tournament.id,))
        return [Participation(id=dict['id'], tournament_id=dict['tournament_id'], player_id=dict['player_id']) for dict in result]
