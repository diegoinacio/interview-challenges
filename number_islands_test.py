import unittest
from number_islands import numIslandsC4, numIslandsC8


GRID01 = [
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 1, 0, 0],
    [ 0, 0, 1, 0, 1, 0],
    [ 0, 0, 0, 0, 1, 0],
    [ 0, 0, 0, 0, 0, 0]
]

GRID02 = [
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1]
]

GRIDCUSTOM = [
    [ 0, 1, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 0, 0, 1, 0, 0],
    [ 0, 1, 0, 0, 0, 1, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 1],
    [ 0, 0, 0, 0, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0],
    [ 0, 1, 1, 0, 0, 0, 0, 0]
]


class Test_NumberIslands(unittest.TestCase):
    def test_sample_case1(self):
        self.assertEqual(numIslandsC4(GRID01), 2)
        self.assertEqual(numIslandsC8(GRID01), 1)

    def test_sample_case2(self):
        self.assertEqual(numIslandsC4(GRID02), 7)
        self.assertEqual(numIslandsC8(GRID02), 1)

    def test_custom_case(self):
        self.assertEqual(numIslandsC4(GRIDCUSTOM), 5)
        self.assertEqual(numIslandsC8(GRIDCUSTOM), 4)


if __name__ == '__main__':
    unittest.main()
