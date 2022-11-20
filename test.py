from wsgi import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # Ensure that the login page loads correctly
    def test_login_test(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Log in' in response.data)

    # Ensures login behaves correctly given that the username and password are correct
    def test_successful_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #self.assertTrue(b'You were logged in' in response.data)
    
    # Ensures login behaves correctly given that the username and password are wrong
    def test_unsuccessful_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="wrong", password="admin"), follow_redirects=True)
        self.assertTrue(b'Log in' in response.data)
    
if __name__ == '__main__':
    unittest.main()