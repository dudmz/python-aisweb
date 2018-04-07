# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestChecklistEndpoint(unittest.TestCase):

    def setUp(self):
        self.a = AISWEB('<API_KEY>', '<API_PASS>')

    def test_checklist_endpoint(self):
        self.assertEqual(self.a.checklist().status_code, 200)
