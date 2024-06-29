import mox
import logging
from py_vetlog_logger.create_log import *

class FixedTest(mox.MoxTestBase):
    path = "vetlog.log"
    def test_create_logger(self):
        logger = self.mox.CreateMockAnything()
        
        self.mox.StubOutWithMock(logging, 'getLogger')
        self.mox.StubOutWithMock(logging, 'FileHandler')
        self.mox.StubOutWithMock(logging, 'Formatter')

        logging.getLogger(self.path).AndReturn(logger)
        logging.FileHandler(self.path).AndReturn(logger)
        logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s').AndReturn(logger)
        
        logger.setLevel(logging.INFO)
        logger.addHandler(logger)
        logger.setFormatter(logger)

        self.mox.ReplayAll()
        log = Logger(self.path)

        assert log.logger == logger