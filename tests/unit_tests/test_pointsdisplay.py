from projet_11_oc.tests.conftest import client

def test_valid_booking(client):
    response = client.get('/points_display')
    assert response.status_code == 200
    assert b'Points Display Board' in response.data
