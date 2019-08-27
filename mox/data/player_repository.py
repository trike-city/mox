from mox.models import Player


class PlayerRepository:
    __TABLE_NAME = 'players'

    def __init__(self, database):
        self.database = database

    def create(self, attributes):
        sql = f"""
        INSERT INTO {self.__TABLE_NAME} (firstname, lastname)
        VALUES (%s, %s)
        RETURNING *;
        """
        values = (attributes['firstname'], attributes['lastname'])
        result = self.database.execute(sql, values)
        return self.__create_instance(result[0])

    def find_many(self, ids):
        sql = f'SELECT * FROM {self.__TABLE_NAME} WHERE id in %s;'
        result = self.database.execute(sql, (tuple(ids),))
        return [self.__create_instance(attr) for attr in result]

    def __create_instance(self, attributes):
        return Player(
            id=attributes['id'],
            firstname=attributes['firstname'],
            lastname=attributes['lastname']
        )
