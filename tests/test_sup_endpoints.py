# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestSupEndpoint(unittest.TestCase):

    def setUp(self):
        self.a = AISWEB('<API_KEY>', '<API_PASS>')

    def test_sup_endpoint(self):
        self.assertEqual(self.a.suplementos(
            {'icaoCode': 'SBBR', 'S': 'A'}
        ).status_code, 200)

    def test_sup_no_data_endpoint(self):
        self.assertEqual(self.a.suplementos({}).status_code, 200)
