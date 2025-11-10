# file: test_mathutils.py
import unittest
from mathutils import add, subtract, multiply, divide

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(-2, -5), 3)
        self.assertEqual(subtract(0, 10), -10)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 7), 0)

    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(3, 2), 1.5)

    def test_divide_zero(self):
        # Memastikan error muncul bila membagi dengan nol
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()