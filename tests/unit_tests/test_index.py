"""
Unit test verifies the response of the index route ('/') in the GUDLFT application.
It imports the 'client' fixture from the conftest module to simulate requests to the application.
"""

from projet_11_oc.tests.conftest import client


def test_index_response(client):
    response = client.get("/")
    assert response.status_code == 200
