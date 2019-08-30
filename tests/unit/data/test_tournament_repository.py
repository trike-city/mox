from mox.data import TournamentRepository
from tests.fixtures import database


attributes = {'name': 'TWC'}


def test_create_return_tournament(database):
    repo = TournamentRepository(database)
    tournament = repo.create(attributes)

    assert tournament.id is not None
    assert tournament.name == 'TWC'


def test_create_persist_tournament(database):
    repo = TournamentRepository(database)
    tournament = repo.create(attributes)
    result = database.execute('SELECT * FROM tournaments;')[0]

    assert result['id'] == tournament.id
    assert result['name'] == 'TWC'
