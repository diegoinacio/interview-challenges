import unittest

import os, sys
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from graph_algorithms import *


G = UndirectedGraph()
G.add_edge(0, 1, 21)
G.add_edge(0, 4, 11)
G.add_edge(1, 2, 4)
G.add_edge(1, 3, 43)
G.add_edge(1, 4, 12)
G.add_edge(2, 3, 43)
G.add_edge(3, 4, 11)


class Test_GraphAlgorithms(unittest.TestCase):
    def test_custom_case0(self):
        self.assertEqual(
            G.get_vertex(1),
            [1, 4, {0: 21, 2: 4, 3: 43, 4: 12}]
        )

    def test_custom_case1(self):
        self.assertEqual(
            G.get_vertices(), [
                [0, 2, {1: 21, 4: 11}],
                [1, 4, {0: 21, 2: 4, 3: 43, 4: 12}],
                [2, 2, {1: 4, 3: 43}],
                [3, 3, {1: 43, 2: 43, 4: 11}],
                [4, 3, {0: 11, 1: 12, 3: 11}]
            ]
        )

if __name__ == '__main__':
    unittest.main()
