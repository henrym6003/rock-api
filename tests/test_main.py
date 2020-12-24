import unittest
from main import app
from flask import Response
import json


class RockTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_initialize(self):
        payload = str.encode(". .\n. .\n :T.\n. .\n   .")
        response: Response = self.app.post('/init-world', data=payload, headers={"Content-Type": "text/plain"})
        assert response.status_code == 201

    def test_invalid_char_initialize(self):
        payload = str.encode(". .\n. .\n :U.\n. .\n   .")
        response: Response = self.app.post('/init-world', data=payload, headers={"Content-Type": "text/plain"})
        assert response.status_code == 400

    def test_invalid_content_initialize(self):
        payload = str.encode(". .\n. .\n :T.\n. .\n   .")
        response: Response = self.app.post('/init-world', data=payload, headers={"Content-Type": "application/json"})
        assert response.status_code == 400

    def test_get_world(self):
        payload = str.encode(". .\n. .\n :T.\n. .\n   .")
        response: Response = self.app.post('/init-world', data=payload, headers={"Content-Type": "text/plain"})
        world_uuid = json.loads(response.data)["world_uuid"]
        response: Response = self.app.get('/world/' + world_uuid)
        assert response.data == str.encode("  : \n  T \n.   \n::.:")

    def test_get_world_404(self):
        response: Response = self.app.get('/world/no-exists')
        assert response.status_code == 404




