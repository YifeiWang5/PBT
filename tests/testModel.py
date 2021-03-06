import unittest
from ddt import ddt, data, unpack
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Local import
from exec.PBT_Quadratic import eval, QHat

@ddt
class TestQFunc(unittest.TestCase):

    @data(
        [[0.9, 0.9], -0.42],
        [[1, 0], 0.2],
        [[0, 1], 0.2],
        [[0.5, 0.5], 0.7]
    )

    @unpack
    def test_eval(self, theta, expectedResult):
        self.assertAlmostEqual(eval(theta), expectedResult, places=7)

    @data(
        [[0.9, 0.9], [1, 1], -0.42],
        [[1, 0], [0, 1], 1.2],
    )
    @unpack
    def test_QHat(self, theta, hyperParam, expectedResult):
        self.assertAlmostEqual(QHat(theta, hyperParam), expectedResult, places=7)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()