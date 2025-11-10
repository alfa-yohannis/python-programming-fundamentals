import unittest

def is_even(n: int) -> bool:
    return (n % 2) == 0

def square(x: int) -> int:
    return x * x

class TestAssertionDasar(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(square(3), 9)
        self.assertEqual(square(-4), 16)

    def test_assert_true_false(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

if __name__ == "__main__":
    unittest.main()