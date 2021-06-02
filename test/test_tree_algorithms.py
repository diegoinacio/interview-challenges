import unittest

import os, sys
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from tree_algorithms import *


# Given the binary tree
# 
#           5
#         /   \
#        2     3
#      /  \   / \
#     4    1 9   8
#   /  \        /
#  6    7     10
# 


BT = BinaryTree(5)
BuildTree(BT.root, [
    [2, 3],
    [4, 1],
    [9, 8],
    [6, 7],
    [-1, -1],
    [-1, -1],
    [10, -1],
    [-1, -1],
    [-1, -1],
    [-1, -1]
])
print(BT)


class Test_TreeAlgorithms(unittest.TestCase):
    def test_get_preOrder(self):
        self.assertEqual(
            get_preOrder(BT.root),
            [5, 2, 4, 6, 7, 1, 3, 9, 8, 10]
        )

    def test_get_postOrder(self):
        self.assertEqual(
            get_postOrder(BT.root),
            [6, 7, 4, 1, 2, 9, 10, 8, 3, 5]
        )

    def test_get_inOrder(self):
        self.assertEqual(
            get_inOrder(BT.root),
            [6, 4, 7, 2, 1, 5, 9, 3, 10, 8]
        )

    def test_get_levelOrder(self):
        self.assertEqual(
            get_levelOrder(BT.root),
            [5, 2, 3, 4, 1, 9, 8, 6, 7, 10]
        )

    def test_get_height(self):
        self.assertEqual(get_height(BT.root), 3)


if __name__ == '__main__':
    unittest.main()
