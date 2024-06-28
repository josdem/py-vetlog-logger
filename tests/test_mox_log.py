import mox
import os

class TestOs(mox.MoxTestBase):
    path = '/mox/path'
    def test_getcwd(self):
        self.mox.StubOutWithMock(os, 'getcwd')

        os.getcwd().AndReturn('/mox/path')

        self.mox.replay_all()
        assert os.getcwd() == '/mox/path'
        self.mox.verify_all()