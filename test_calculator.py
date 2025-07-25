# test_calculator.py

import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -2), -1)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(1, -2), 3)

if __name__ == "__main__":
    unittest.main()
