from mox.models import Participation


class ParticipationRepository:
    __TABLE_NAME = 'participations'

    def __init__(self, database):
        self.database = database

    def create_many(self, tournament, players):
        self.__create_participations(tournament=tournament, players=players)
        return self.find_by_tournament(tournament)

    def find_by_tournament(self, tournament):
        sql = f'SELECT * FROM {self.__TABLE_NAME} WHERE tournament_id = %s;'
        result = self.database.execute(sql, (tournament.id,))
        return [Participation.build(attribute) for attribute in result]

    def __create_participations(self, tournament, players):
        sql = f"""
        INSERT INTO {self.__TABLE_NAME} (tournament_id, player_id)
        VALUES (%s, %s);
        """
        values = [(tournament.id, p.id,) for p in players]
        self.database.execute(sql, values)
