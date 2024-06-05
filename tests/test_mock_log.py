from unittest.mock import MagicMock
from python.create_log import *
import unittest

class FixedTest(unittest.TestCase):
    path = "vetlog.log"
    def test_create_logger(self):
        log = Logger(self.path)
        logger = MagicMock()
        log.get_logger = MagicMock(return_value=logger)
        logger.setLevel.assert_called_once_with(logging.INFO)
       