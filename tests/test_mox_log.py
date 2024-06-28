import mox
import os

class TestOs:
    def test_getcwd(self):
        m = mox.Mox()

        m.stubout(os, 'getcwd')
        # calls
        os.getcwd().returns('/mox/path')

        m.replay_all()
        assert os.getcwd() == '/mox/path'
        


if __name__ == '__main__':
    import unittest
    unittest.main()