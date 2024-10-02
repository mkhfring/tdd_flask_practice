import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Test that the home page returns a 200 status code
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_content(self):
        # Test that the home page returns the correct content
        result = self.app.get('/')
        self.assertEqual(result.data.decode(), 'Welcome to the Flask App!')   
    
    def test_multipy_endpoint(self):
        # Test the multiply endpoint with sample inputs
        data = {'a': 5, 'b': 10}
        result = self.app.post('/multiply', json=data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, {'result': 50})

if __name__ == '__main__':
    unittest.main()