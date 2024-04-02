"""
This file contains integration tests for the GUDLFT web application, which tests the interaction
of multiple components together.

 The integration test covers the following scenarios:
- Testing the home page to ensure it loads successfully and displays the welcome message.
- Testing form submission with a valid email address.
- Testing reservation for an existing competition and club.
- Testing purchasing places with valid data.
- Testing logout functionality.
"""

from flask import Flask, url_for

from projet_11_oc.server import app, loadClubs, loadCompetitions
from projet_11_oc.tests.conftest import client


def test_integration(client):
    # Load initial data
    clubs = loadClubs()
    competitions = loadCompetitions()

    # Test home page
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

    # Test form submission with valid email address
    response = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data

    # Test reservation for an existing competition and club
    response = client.get("/book/Spring%20Festival/Simply%20Lift")
    assert response.status_code == 200
    assert b"How many places?" in response.data

    # Test purchasing places with valid data
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
    )
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data

    # Test logout
    response = client.get("/logout")
    assert response.status_code == 302
    assert response.location == "/"
