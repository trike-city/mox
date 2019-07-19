import pytest
import json

from tests.fixtures import client


def test_create(client):
    data = {'firstname': 'Binom', 'lastname': 'Missieu'}

    response = client.post('/players',
                           data=json.dumps(data),
                           content_type='application/json')

    assert response.status_code == 201
    assert response.data == b'{"firstname":"Binom","lastname":"Missieu"}\n'
