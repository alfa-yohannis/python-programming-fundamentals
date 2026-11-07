# file: test_fungsi.py
import unittest
from fungsi import add   # mengimpor fungsi yang akan diuji

class TestAddFunction(unittest.TestCase):
    def test_penjumlahan_positif(self):
        self.assertEqual(add(2, 3), 5)

    def test_penjumlahan_negatif(self):
        self.assertEqual(add(-4, -6), -10)

    def test_penjumlahan_nol(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()