from projet_11_oc.tests.conftest import client

def test_valid_booking(client):
    response = client.get('/book/Spring%20Festival/Simply%20Lift')
    assert response.status_code == 200
    assert b'Booking for' in response.data
    assert b'Spring Festival' in response.data


# def test_invalid_booking(client):
#     response = client.get('/book/non_existing_competition/non_existing_club')
#     assert response.status_code == 200
#     assert b'Something went wrong-please try again' in response.data
