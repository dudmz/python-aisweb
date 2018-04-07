# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestMetEndpoint(unittest.TestCase):

    def setUp(self):
        self.a = AISWEB('<API_KEY>', '<API_PASS>')

    def test_met_endpoint(self):
        self.assertEqual(self.a.met({'icaoCode': 'SBBR'}).status_code, 200)

    def test_no_data_met_endpoint(self):
        self.assertEqual(self.a.met({}), None)

