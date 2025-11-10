# file: test_fungsi.py
import unittest
from fungsi2 import add, subtract

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 7), -7)
        self.assertEqual(subtract(-2, -3), 1)

if __name__ == "__main__":
    unittest.main()