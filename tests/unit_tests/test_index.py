from projet_11_oc.tests.conftest import client


def test_index_response(client):
    response = client.get('/')
    assert response.status_code == 200