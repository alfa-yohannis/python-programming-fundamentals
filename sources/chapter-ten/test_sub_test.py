import unittest

def multiply(a, b):
    return a * b

class TestSubTest(unittest.TestCase):
    def test_multiply_variatif(self):
        # Beberapa kasus uji dalam satu metode
        kasus = [
            (2, 3, 6),
            (0, 10, 0),
            (-2, 4, -8),
            (1.5, 2, 3.0),
        ]
        for a, b, expected in kasus:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiply(a, b), expected)

if __name__ == "__main__":
    unittest.main()