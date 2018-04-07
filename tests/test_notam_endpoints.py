# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestNotamEndpoint(unittest.TestCase):

    def setUp(self):
        self.a = AISWEB('<API_KEY>', '<API_PASS>')

    def test_notam_endpoint(self):
        self.assertEqual(self.a.notam(
            {'icaoCode': ['SBBR', 'SBGL'], 'dist': 'N'}
        ).status_code, 200)

    def test_notam_no_data_endpoint(self):
        self.assertEqual(self.a.notam({}).status_code, 200)
