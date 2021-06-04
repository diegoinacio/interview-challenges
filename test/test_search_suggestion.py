import unittest

import os
import sys
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from search_suggestion import searchSuggestions


class Test_RunningMedian(unittest.TestCase):
    def test_sample_case0(self):
        self.assertEqual(
            searchSuggestions(
                ["baggage", "bags", "banner", "box", "cloths"], 
                "bags"
            ), [
                ["baggage", "bags", "banner"],
                ["baggage", "bags"],
                ["bags"]
            ]
        )

    def test_sample_case1(self):
        self.assertEqual(
            searchSuggestions(
                ["coddle", "coddles", "code", "codephone", "codes"], 
                "coddle"
            ), [
                ["coddle", "coddles", "code"],
                ["coddle", "coddles", "code"],
                ["coddle", "coddles"],
                ["coddle", "coddles"],
                ["coddle", "coddles"]
            ]
        )


if __name__ == "__main__":
    unittest.main()
