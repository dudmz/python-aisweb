# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestFixesEndpoint(unittest.TestCase):

    def setUp(self):
        self.a = AISWEB('<API_KEY>', '<API_PASS>')

    def test_fixes_endpoint(self):
        self.assertEqual(self.a.fixos().status_code, 200)
