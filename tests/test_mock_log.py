from unittest.mock import MagicMock
from python.create_log import *
import unittest

class FixedTest(unittest.TestCase):
    path = "vetlog.log"
    def test_create_logger(self):
        log = Logger(self.path)
        logger = MagicMock()
        log.logger = logger
        assert log.get_logger() == logger
       