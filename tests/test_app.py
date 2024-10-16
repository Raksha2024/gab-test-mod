# tests/test_app.py
import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_login_page(self):
        """Test if the login page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)  # Adjust based on your HTML content

    def test_healthcheck(self):
        """Test the healthcheck endpoint."""
        response = self.app.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['description'], "A simple login application.")
        self.assertEqual(json_data['version'], "1.0")
        self.assertIsInstance(json_data['last_commit_sha'], str)  # Check that it's a string

if __name__ == '__main__':
    unittest.main()