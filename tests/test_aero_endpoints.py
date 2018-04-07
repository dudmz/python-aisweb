# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestAeroEndpoint(unittest.TestCase):

    def setUp(self):
        self.a = AISWEB('<API_KEY>', '<API_PASS>')

    def test_aero_endpoint(self):
        self.assertEqual(self.a.aero({'icaoCode': 'SBBR'}).status_code, 200)

    # May fail in certain times because the system might be updating its data.
    # So there's nothing wrong with the code, it just returns a response.text
    # "em atualização (updating)".
    def test_aero_no_data_endpoint(self):
        self.assertEqual(self.a.aero({}), None)
