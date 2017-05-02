import sys
import os
project_dir = os.path.abspath(
    os.path.join(os.path.dirname( __file__ ), '..', '..', '..'))
sys.path.insert(0, project_dir)
print(sys.path)
from server.python.server import app
import unittest

class TestServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        response_text = rv.data.decode('UTF-8')
        self.assertEqual('Watson Discovery Service Starter Kit', response_text)

if __name__ == '__main__':
    unittest.main()