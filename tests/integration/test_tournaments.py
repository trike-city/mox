import pytest
import json

from tests.client import client


def test_create(client):
    data = {'name': 'Binomville', 'competitors': []}

    response = client.post('/tournaments',
                           data=json.dumps(data),
                           content_type='application/json')

    assert response.status_code == 201
    assert response.data == b'{"name":"Binomville"}\n'
