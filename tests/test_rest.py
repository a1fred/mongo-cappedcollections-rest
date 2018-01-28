import unittest
from webapp.app import app


class RestApiTests(unittest.TestCase):
    def test_index_returns_200(self):
        request, response = app.test_client.get('/')
        assert response.status == 200

    def test_index_put_not_allowed(self):
        request, response = app.test_client.put('/')
        assert response.status == 405
