from mox.models import Player
from .record_finder import RecordFinder


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

    def find_one(self, id):
        result = self.__finder.find_one(id)
        return self.__create_instance(result)

    def find_many(self, ids):
        result = self.__finder.find_many(ids)
        return [self.__create_instance(attr) for attr in result]

    def __create_instance(self, attributes):
        return Player(
            id=attributes['id'],
            firstname=attributes['firstname'],
            lastname=attributes['lastname']
        )

    @property
    def __finder(self):
        return RecordFinder(database=self.database, table=self.__TABLE_NAME)
