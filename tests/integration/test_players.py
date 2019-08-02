import json

from tests.fixtures import client


def test_create(client):
    data = {'firstname': 'Binom', 'lastname': 'Missieu'}

    response = client.post('/players', data=json.dumps(data), content_type='application/json')
    player_id = client.database.execute('SELECT (id) FROM players;')[0]['id']

    assert response.status_code == 201
    assert json.loads(response.data) == {
        "id": player_id,
        "firstname": "Binom",
        "lastname": "Missieu"
    }
