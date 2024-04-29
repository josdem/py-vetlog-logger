import os
import unittest
from python.create_log import *

class FixedTest(unittest.TestCase):
    path = "vetlog.log"
    def test_create_logger(self):
        Logger(self.path)
        self.assertTrue(os.path.isfile(self.path))