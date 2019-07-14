import pytest

from tests.client import client


def test_create(client):
    data = { 'firstname': 'Binom', 'lastname': 'Missieu' }
    response = client.post('/players', data=data)

    assert response.status_code == 201
    assert response.data == b'{"firstname":"Binom","lastname":"Missieu"}\n'
