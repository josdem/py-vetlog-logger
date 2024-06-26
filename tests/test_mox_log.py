import mox
import os

class FixedTest(mox.MoxTestBase):
    def test_get_cwd(self):
        self.mox.StubOutWithMock(os, 'getcwd')
        os.getcwd().AndReturn('/mox/path')

        self.mox.ReplayAll()
        self.assertEqual(os.getcwd(), '/mox/path')
        self.mox.VerifyAll()

if __name__ == '__main__':
    import unittest
    unittest.main()