# file: mathutils.py

def add(a, b):
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b

def subtract(a, b):
    """Mengembalikan hasil pengurangan a - b."""
    return a - b

def multiply(a, b):
    """Mengembalikan hasil perkalian a * b."""
    return a * b

def divide(a, b):
    """Membagi a dengan b. Jika b = 0, munculkan ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("tidak dapat membagi dengan nol")
    return a / b