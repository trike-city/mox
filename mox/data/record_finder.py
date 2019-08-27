class RecordFinder:
    def __init__(self, database, table):
        self.database = database
        self.table = table

    def find_many(self, ids):
        sql = f'SELECT * FROM {self.table} WHERE id in %s;'
        values = (tuple(ids),)
        return self.database.execute(sql, values)
