# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestSunEndpoint(unittest.TestCase):

    def setUp(self):
        self.a = AISWEB('<API_KEY>', '<API_PASS>')

    def test_sun_no_date_endpoint(self):
        self.assertEqual(self.a.sol({'icaoCode': 'SBBR'}).status_code, 200)

    def test_sun_with_date_endpoint(self):
        self.assertEqual(self.a.sol(
            {'icaoCode': 'SBBR', 'dt_i': '2018-03-26', 'dt_f': '2018-03-28'}
        ).status_code, 200)

    def test_sun_no_data_endpoint(self):
        self.asserteEqual(self.a.sol().status_code, 200)
