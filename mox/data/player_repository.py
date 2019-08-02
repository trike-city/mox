from mox.models import Player


class PlayerRepository:
    __TABLE_NAME = 'players'

    def __init__(self, database):
        self.database = database

    def create(self, attributes):
        sql = f'INSERT INTO {self.__TABLE_NAME} (firstname, lastname) VALUES (%s, %s) RETURNING id;'
        values = (attributes['firstname'], attributes['lastname'])
        result = self.database.execute(sql, values)
        return self.__create_instance(result[0]['id'], attributes)

    def __create_instance(self, id, attributes):
        return Player(
            id=id,
            firstname=attributes['firstname'],
            lastname=attributes['lastname']
        )
