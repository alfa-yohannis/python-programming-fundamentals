# file: test_bank_account.py
import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """Kumpulan test untuk menguji perilaku class BankAccount."""

    def setUp(self):
        """Menyiapkan objek uji sebelum setiap test dijalankan."""
        self.account = BankAccount("Alice", 100.0)

    def tearDown(self):
        """Membersihkan resource setelah test selesai."""
        self.account = None

    def test_deposit_berhasil(self):
        saldo_baru = self.account.deposit(50.0)
        self.assertEqual(saldo_baru, 150.0)
        self.assertEqual(self.account.get_balance(), 150.0)

    def test_deposit_tidak_valid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10.0)

    def test_withdraw_berhasil(self):
        saldo_baru = self.account.withdraw(40.0)
        self.assertEqual(saldo_baru, 60.0)
        self.assertEqual(self.account.get_balance(), 60.0)

    def test_withdraw_melebihi_saldo(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200.0)

    def test_withdraw_nilai_negatif(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-5.0)

    def test_get_balance_awal(self):
        self.assertEqual(self.account.get_balance(), 100.0)

if __name__ == "__main__":
    unittest.main()