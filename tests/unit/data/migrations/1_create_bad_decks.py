def up(database):
    database.execute('CREATE TABLE bad_decks ();')


def down(database):
    database.execute('DROP TABLE bad_decks;')
