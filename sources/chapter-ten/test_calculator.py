# file: test_calculator.py
import unittest
from calculator import Calculator

class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        # Dipanggil sebelum setiap test_*
        # Siapkan objek baru agar setiap test terisolasi
        self.calc = Calculator()

    def tearDown(self):
        # Dipanggil setelah setiap test_*
        # Biasanya untuk cleanup resource; di sini cukup reset referensi
        self.calc = None

    # ---------- Instance methods ----------
    def test_add_mengembalikan_hasil_dan_update_memory(self):
        hasil = self.calc.add(2, 3)
        self.assertEqual(hasil, 5.0)
        self.assertEqual(self.calc.memory, 5.0)

    def test_divide_normal(self):
        hasil = self.calc.divide(10, 2)
        self.assertEqual(hasil, 5.0)
        self.assertEqual(self.calc.memory, 5.0)

    def test_divide_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)

    # SubTest untuk variasi input add
    def test_add_dengan_variansi_input(self):
        kasus = [
            (0, 0, 0.0),
            (1, -1, 0.0),
            (2.5, 0.5, 3.0),
            (-3, -7, -10.0),
        ]
        for a, b, expected in kasus:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)

    # ---------- Static method ----------
    def test_is_even(self):
        # Bisa dipanggil via kelas atau instance
        self.assertTrue(Calculator.is_even(2))
        self.assertFalse(self.calc.is_even(3))

    # ---------- Class method ----------
    def test_from_string_valid(self):
        c = Calculator.from_string("  42.5 ")
        self.assertIsInstance(c, Calculator)
        self.assertEqual(c.memory, 42.5)

    def test_from_string_invalid_raises(self):
        with self.assertRaises(ValueError):
            Calculator.from_string("bukan-angka")

if __name__ == "__main__":
    unittest.main()