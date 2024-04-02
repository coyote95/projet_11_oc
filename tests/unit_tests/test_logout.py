"""
Unit test for user logout functionality in the GUDLFT web application.
It imports the 'client' fixture from the conftest module to simulate requests to the application.
"""

from projet_11_oc.tests.conftest import client


def test_logout(client):
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Welcome" in response.data
