import unittest
from .python_aisweb import AISWEB

class ApiAuthTest(unittest.Testcase):

    def setUp(self):
        self.a = AISWEB('Insert API Token', 'Insert API Password')


