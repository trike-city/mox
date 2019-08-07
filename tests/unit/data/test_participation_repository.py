from mox.data import ParticipationRepository
from mox.models import Tournament, Player
from tests.fixtures import database


tournament = Tournament(id=5, name='Monthly March')
players = [
    Player(id=1, firstname='Binom', lastname='Missieu'),
    Player(id=2, firstname='Julien', lastname='Pouliot')
]


def test_create_many_returns_participation(database):
    repo = ParticipationRepository(database)
    participations = repo.create_many(tournament=tournament, players=players)
    assert len(players) == len(participations)
    assert [p.tournament_id for p in participations] == [5, 5]
    assert [p.player_id for p in participations] == [1, 2]


def test_create_many_persists_participations(database):
    repo = ParticipationRepository(database)
    repo.create_many(tournament=tournament, players=players)
    result = database.execute('SELECT * FROM participations;')
    assert len(result) == len(players)


def test_find_by_tournament(database):
    repo = ParticipationRepository(database)
    repo.create_many(tournament=tournament, players=players)
    result = repo.find_by_tournament(tournament)
    assert len(result) == 2
    assert [p.player_id for p in result] == [1, 2]
