from projet_11_oc.tests.conftest import client


def test_show_summary_valid_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_show_summary_invalid_email(client):
    response = client.post('/showSummary', data={'email': 'invalid@example.com'})
    assert response.status_code == 200
    assert b'<p>Sorry, that email wasn&#39;t found.</p>' in response.data