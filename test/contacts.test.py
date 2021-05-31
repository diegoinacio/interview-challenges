import unittest

import os, sys
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from contacts import *


class Test_Contacts(unittest.TestCase):
    def test_sample_case0(self):
        self.assertEqual(
            contacts([
                ["add", "hack"],
                ["add", "hackerrank"],
                ["find", "hac"],
                ["find", "hak"]
            ]),
            [2, 0]
        )

    def test_sample_case1(self):
        self.assertEqual(
            contacts([
                ["add", "ed"],
                ["add", "eddie"],
                ["add", "edward"],
                ["find", "ed"],
                ["add", "edwina"],
                ["find", "edw"],
                ["find", "a"]
            ]),
            [3, 2, 0]
        )

    def test_custom_case0(self):
        self.assertEqual(
            contacts([
                ["add", "diego"],
                ["add", "diogo"],
                ["add", "diogenes"],
                ["find", "die"],
                ["find", "dio"]
            ]),
            [1, 2]
        )

    def test_custom_case1(self):
        self.assertEqual(
            contacts([
                ["add", "diego"],
                ["add", "diogo"],
                ["find", "die"],
                ["add", "diogenes"],
                ["find", "dio"],
                ["add", "diegones"],
                ["add", "dialogo"],
                ["find", "die"],
                ["find", "dio"],
                ["find", "dia"]
            ]),
            [1, 2, 2, 2, 1]
        )


if __name__ == '__main__':
    unittest.main()
