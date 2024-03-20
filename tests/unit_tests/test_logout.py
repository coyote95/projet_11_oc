from projet_11_oc.tests.conftest import client

def test_logout(client):
    response = client.get('/logout',follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome' in response.data

