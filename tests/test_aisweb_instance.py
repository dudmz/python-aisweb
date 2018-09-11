# -*- coding: utf-8 -*-

import unittest

from python_aisweb import AISWEB


class TestAISWEBInstance(unittest.TestCase):

    def test_instance_without_keys(self):
        with self.assertRaises(TypeError):
            AISWEB()

    def test_instance_empty_args_string(self):
        with self.assertRaises(TypeError):
            AISWEB('', '')

    def test_instance_empty_args_list(self):
        with self.assertRaises(TypeError):
            AISWEB([], [])

    def test_instance_empty_args_dict(self):
        with self.assertRaises(TypeError):
            AISWEB({}, {})

    def test_instance_repr_numeric_empty_arg(self):
        with self.assertRaises(TypeError):
            AISWEB(0, 0)

    def test_instance_numeric_args(self):
        with self.assertRaises(TypeError):
            AISWEB(123, 123)
