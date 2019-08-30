from mox.models import Tournament


class TournamentRepository:
    __TABLE_NAME = 'tournaments'

    def __init__(self, database):
        self.database = database

    def create(self, attributes):
        sql = f'INSERT INTO {self.__TABLE_NAME} (name) VALUES (%s) RETURNING *;'
        values = (attributes['name'],)
        result = self.database.execute(sql, values)
        return self.__create_instance(result[0])

    def __create_instance(self, attributes):
        return Tournament(id=attributes['id'], name=attributes['name'])
