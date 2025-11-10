# file: calculator.py

class Calculator:
    def __init__(self, memory: float = 0.0):
        # state internal: menyimpan nilai terakhir
        self.memory = float(memory)

    # -------- Instance methods --------
    def add(self, a: float, b: float) -> float:
        """Menjumlahkan a dan b, memperbarui memory, dan mengembalikan hasil."""
        result = float(a) + float(b)
        self.memory = result
        return result

    def divide(self, a: float, b: float) -> float:
        """Membagi a dengan b. Memunculkan ZeroDivisionError jika b == 0."""
        if b == 0:
            raise ZeroDivisionError("pembagian dengan nol")
        result = float(a) / float(b)
        self.memory = result
        return result

    # -------- Static method --------
    @staticmethod
    def is_even(n: int) -> bool:
        """Mengembalikan True jika n genap, False jika ganjil."""
        return (n % 2) == 0

    # -------- Class method --------
    @classmethod
    def from_string(cls, s: str) -> "Calculator":
        """
        Alternate constructor: membuat Calculator dari string angka.
        Jika string tidak valid, ValueError.
        """
        try:
            val = float(s.strip())
        except Exception as e:
            raise ValueError(f"nilai tidak valid: {s}") from e
        return cls(memory=val)