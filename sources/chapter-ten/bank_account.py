# file: bank_account.py

class BankAccount:
    """Kelas sederhana untuk merepresentasikan rekening bank."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Menambah saldo sebesar amount."""
        if amount <= 0:
            raise ValueError("Jumlah setoran harus positif.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        """Mengurangi saldo sebesar amount, jika saldo cukup."""
        if amount <= 0:
            raise ValueError("Jumlah penarikan harus positif.")
        if amount > self.balance:
            raise ValueError("Saldo tidak mencukupi.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Mengembalikan saldo saat ini."""
        return self.balance