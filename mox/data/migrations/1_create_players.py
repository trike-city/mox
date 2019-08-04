def up(database):
    database.execute("""
    CREATE SEQUENCE players_id_seq;

    CREATE TABLE players (
        id integer NOT NULL DEFAULT nextval('players_id_seq'),
        firstname VARCHAR (50),
        lastname VARCHAR (50)
    );

    ALTER SEQUENCE players_id_seq
    OWNED BY players.id;
    """)


def down(database):
    database.execute('DROP TABLE players;')