import os
import unittest
from py_vetlog_logger.create_log import *

class FixedTest(unittest.TestCase):
    path = "vetlog.log"
    def test_create_logger(self):
        log = Logger(self.path)
        test_logger = log.get_logger()
        test_logger.info("Test log")
        assert os.path.exists(self.path)
        file = open(self.path, 'r')
        assert "Test log" in file.read()
        file.close()
        