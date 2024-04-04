"""
This file contains a Locust user class that defines load testing tasks for the GUDLFT web application.
It imports the HttpUser and task classes from the Locust library. The tasks include:
- 'home': Sends a GET request to the home page ("/") of the GUDLFT application.
- 'show_summary': Sends a POST request to the '/showSummary' endpoint with a sample email payload.
"""

from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def home(self):
        self.client.get("/")

    @task
    def show_summary(self):
        self.client.post("/showSummary", {"email": "john@simplylift.co"})
