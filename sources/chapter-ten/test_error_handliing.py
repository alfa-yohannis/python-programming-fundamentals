import unittest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("pembagian dengan nol tidak diperbolehkan")
    return a / b

class TestErrorHandling(unittest.TestCase):
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_zero(self):
        # Bentuk konteks
        with self.assertRaises(ZeroDivisionError):
            divide(4, 0)

    def test_divide_zero_pakai_lambda(self):
        # Bentuk pemanggilan langsung
        self.assertRaises(ZeroDivisionError, divide, 1, 0)

if __name__ == "__main__":
    unittest.main()