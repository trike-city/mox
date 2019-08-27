def up(database):
    database.execute("""
    CREATE SEQUENCE participations_id_seq;

    CREATE TABLE participations (
        id integer NOT NULL DEFAULT nextval('participations_id_seq'),
        player_id integer NOT NULL,
        tournament_id integer NOT NULL
    );

    ALTER SEQUENCE participations_id_seq
    OWNED BY participations.id;
    """)


def down(database):
    database.execute('DROP TABLE participations;')
