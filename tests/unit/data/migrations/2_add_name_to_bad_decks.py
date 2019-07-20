def up(database):
    database.execute('ALTER TABLE bad_decks ADD COLUMN name TEXT;')


def down(database):
    database.execute('ALTER TABLE bad_decks DROP COLUMN name;')
