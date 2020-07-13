import unittest
from ddt import ddt, data, unpack
import sys
import os
import numpy as np
from functools import reduce


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Local import
from exec.PBT_Quadratic import step, ready, exploit, explore
from src.worker import Worker

@ddt
class TestPBTQuadratic(unittest.TestCase):
    def setUp(self):
        self.workers = [
            Worker(init_hyperParam=[0, 1], init_theta=[0.9, 0.9]),
            Worker(init_hyperParam=[1, 0], init_theta=[0.5, 0.5])
        ]

    def assertNestedListEqual(self, calculatedList, expectedList, places=7):
        self.assertEqual(len(calculatedList), len(expectedList))
        self.assertTrue(reduce(lambda b1,b2: b1 and b2, map(lambda e1,e2: e1==e2, calculatedList, expectedList), True))


    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)

    @data(
        # [16, 1],
        # [5, 0],
        # [20, 1],
        # [30, 0]
    )
    @unpack
    def test_step(self, theta, hyperParam, expectedResult):
        self.assertEqual(step(theta, hyperParam), expectedResult)  # Almost

    @data(
        [16, 1],
        [5, 0],
        [20, 1],
        [30, 0]
    )
    @unpack
    def test_ready(self, step, expectedResult):
        self.assertEqual(ready(0, step, 0), expectedResult) # Almost

    @data(
        [[[1, 0], [0.5, 0.5]]]
    )

    @unpack
    def test_exploit(self, expectedResult):
        output = exploit(self.workers[0].hyperParam, self.workers[0].theta, self.workers[0].p, self.workers)
        calculatedResult = [output[0], output[1]]
        self.assertNestedListEqual(calculatedResult, expectedResult, places=7)

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
