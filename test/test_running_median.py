import unittest

import os, sys
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from running_median import runningMedian

class Test_RunningMedian(unittest.TestCase):
    def test_sample_case0(self):
        self.assertEqual(
            runningMedian([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ['1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5', '5.0', '5.5']
        )

    def test_custom_case(self):
        self.assertEqual(runningMedian([]), [])
        self.assertEqual(
            runningMedian([16, 8, 2, 4, 32]),
            ['16.0', '12.0', '8.0', '6.0', '8.0']
        )


if __name__ == '__main__':
    unittest.main()
