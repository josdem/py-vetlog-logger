import mox
import os
import logging
from py_vetlog_logger.create_log import *

class TestOs(mox.MoxTestBase):
    path = "/mox/path"
    mock_logger = mox.MockAnything()
    def test_getcwd(self):
        self.mox.StubOutWithMock(logging, 'getLogger')

        logging.getLogger().AndReturn(self.mock_logger)

        log = Logger(self.path)

        self.mox.replay_all()
        assert log.get_logger() == self.mock_logger