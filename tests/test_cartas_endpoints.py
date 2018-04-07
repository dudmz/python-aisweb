# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestCartasEndpoint(unittest.TestCase):

    def setUp(self):
        self.a = AISWEB('<API_KEY>', '<API_PASS>')

    def test_cartas_endpoint(self):
        self.assertEqual(self.a.cartas(
            {'icaoCode': 'SBBR', 'tipo': 'ADC'}
        ).status_code, 200)

    def test_cartas_no_data_endpoint(self):
        self.assertEqual(self.a.cartas({}).status_code, 200)
