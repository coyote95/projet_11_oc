from flask import Flask, url_for
from flask_testing import TestCase
from projet_11_oc.server import app, loadClubs, loadCompetitions

class TestIntegration(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'secret_key'
        return app

    def test_integration(self):
        # Charge les données initiales
        clubs = loadClubs()
        competitions = loadCompetitions()

        # Teste la page d'accueil
        response = self.client.get('/')
        self.assert_template_used('index.html')

        # Teste la soumission du formulaire avec une adresse email valide
        response = self.client.post('/showSummary', data={'email': 'john@simplylift.co'})
        self.assert_template_used('welcome.html')

        # Teste la réservation pour une compétition et un club existants
        response = self.client.get('/book/Spring%20Festival/Simply%20Lift')
        self.assert_template_used('booking.html')

        # Teste l'achat de places avec des données valides
        response = self.client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '2'})
        self.assert_message_flashed('Great-booking complete!')

        # Teste la déconnexion
        response = self.client.get('/logout')
        # self.assert_redirects(response, '/')
        self.assertEqual(response.status_code, 302)


