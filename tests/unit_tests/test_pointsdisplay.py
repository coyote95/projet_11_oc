"""
Unit test for the points display board in the GUDLFT web application.
It imports the 'client' fixture from the conftest module to simulate requests to the application.
"""

from projet_11_oc.tests.conftest import client


def test_points_display(client):
    response = client.get("/points_display")
    assert response.status_code == 200
    assert b"Points Display Board" in response.data
