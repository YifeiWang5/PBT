import unittest
from ddt import ddt, data, unpack
import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Local import
from exec.PBT_Quadratic import ready, exploit, explore
from src.PBT_Quadratic.worker import Worker

@ddt
class TestPBTQuadratic(unittest.TestCase):
    def setUp(self):
        self.workers = [
            Worker(init_theta=[0.9, 0.9], init_hyperParam=[0, 1]),
            Worker(init_theta=[0.9, 0.9], init_hyperParam=[1, 0])
        ]

    @data(
        [16, 1],
        [5, 0],
        [20, 1],
        [30, 0]
    )
    @unpack
    def test_ready(self, step, expectedResult):
        self.assertEqual(ready(0, step, 0), expectedResult) # Almost

    # @data(
    #
    # )
    #
    # @unpack
    # def test_exploit(self, theta, expectedResult):
    #     self.assertAlmostEqual(exploit(self.workers[0].hyperParam), expectedResult, places=7)

    @data(
        [[1, 1]],
        [[1, 0]],
        [[0, 1]],
        [[0.5, 0.5]]
    )
    @unpack
    def test_explore(self, hPrime):
        thetaPrime = [0.9, 0.9]
        possible_factor_list = [[1.2, 1.2], [0.8, 0.8], [1.2, 0.8], [0.8, 1.2]]
        expected_results = [[[i[0] * hPrime[0], i[1] * hPrime[1]], thetaPrime] for i in possible_factor_list]
        output = explore(hPrime, thetaPrime, self.workers)
        calculatedResult = [[output[0], output[1]]]
        self.assertTrue(np.all(item in expected_results for item in calculatedResult))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
