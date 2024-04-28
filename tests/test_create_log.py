import os
import unittest
from python.create_log import create_log

class FixedTest(unittest.TestCase):
    def test_create_log(self):
        create_log()
        self.assertTrue(os.path.isfile("vetlog.log"))