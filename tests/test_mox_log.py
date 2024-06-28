import mox
import os

class TestOs(mox.MoxTestBase):
    def test_getcwd(self):
        self.mox.StubOutWithMock(os, 'getcwd')
        # calls
        os.getcwd().AndReturn('/mox/path')

        self.mox.ReplayAll()
        self.assertEqual(os.getcwd(), '/mox/path')
        self.mox.VerifyAll()


if __name__ == '__main__':
    import unittest
    unittest.main()