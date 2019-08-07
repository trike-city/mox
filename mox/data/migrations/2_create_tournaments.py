def up(database):
    database.execute("""
    CREATE SEQUENCE tournaments_id_seq;

    CREATE TABLE tournaments(
        id integer NOT NULL DEFAULT nextval('tournaments_id_seq'),
        name VARCHAR (100)
    );

    ALTER SEQUENCE tournaments_id_seq
    OWNED BY tournaments.id;
    """)


def down(database):
    database.execute('DROP TABLE tournaments;')
