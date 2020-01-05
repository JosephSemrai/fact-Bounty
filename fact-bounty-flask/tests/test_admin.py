import os
import unittest
import tempfile
import json

FLASKR = __import__('fact-bounty-flask')


class Test_Crawler(unittest.TestCase):
    def setUp(self):
        self.db_fd,
        FLASKR.config['SQLALCHEMY_DATABASE_URI'] = tempfile.mkstemp()
        FLASKR.testing = True
        self.app = FLASKR.app.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(FLASKR.config['SQLALCHEMY_DATABASE_URI'])

    def test_fetch_all_jobs_200(self):
        """Get System Panel Information"""
        response = self.app.get('/api/admin/system')
        res = response.data.decode('ASCII')
        res = json.loads(res)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], 'Data fetched successfully!')
        self.assertTrue(isinstance(res['data'], (dict)))
