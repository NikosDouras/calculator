# tests/test_server.py

import unittest
from app.server import app

class TestServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.get('/add?a=1&b=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 3.0)

    def test_subtract(self):
        response = self.app.get('/subtract?a=5&b=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 3.0)

    def test_multiply(self):
        response = self.app.get('/multiply?a=3&b=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 12.0)

    def test_divide(self):
        response = self.app.get('/divide?a=10&b=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 5.0)

    def test_divide_by_zero(self):
        response = self.app.get('/divide?a=10&b=0')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == "__main__":
    unittest.main()
