import unittest
import backend
import os
import json

class NBATestCase(unittest.TestCase):
    def setUp(self):
        self.db_file = 'test_nba_players.db'
        backend.app.config['DATABASE'] = self.db_file # overwrite config: let app use test database
        backend.app.config['TESTING'] = True
        self.app = backend.app.test_client()
        backend.init_db()

    def tearDown(self):
        # delete the test database
        os.unlink(self.db_file)

    def test_one(self):
        response = self.app.get('/')
        players = json.loads(response.data)
        self.assertEqual(len(players['results']), 444)
