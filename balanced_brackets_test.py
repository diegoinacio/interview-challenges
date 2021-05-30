import unittest
from balanced_brackets import *


class Test_BalancedBrackets(unittest.TestCase):
    def test_sample_case0(self):
        self.assertEqual(isBalanced(r'{[()]}'), "YES")
        self.assertEqual(isBalanced(r'{[(])}'), "NO")
        self.assertEqual(isBalanced(r'{{[[(())]]}}'), "YES")

    def test_sample_case1(self):
        self.assertEqual(isBalanced(r'{{([])}}'), "YES")
        self.assertEqual(isBalanced(r'{{)[](}}'), "NO")

    def test_sample_case2(self):
        self.assertEqual(isBalanced(r'{(([])[])[]}'), "YES")
        self.assertEqual(isBalanced(r'{(([])[])[]]}'), "NO")
        self.assertEqual(isBalanced(r'{(([])[])[]}[]'), "YES")

    def test_custom_case(self):
        self.assertEqual(isBalanced(r''), "YES")
        self.assertEqual(isBalanced(r'13'), "YES")
        self.assertEqual(isBalanced(r'([{7}])'), "YES")
        self.assertEqual(isBalanced(r'{[()*15{}]}'), "YES")
        self.assertEqual(isBalanced(r'{[{[{()}]}])'), "NO")


if __name__ == '__main__':
    unittest.main()
