def add(a, b):
    """Mengembalikan hasil penjumlahan a + b"""
    return a + b

def subtract(a, b):
    """Mengembalikan hasil pengurangan a - b"""
    return a - b

def multiply(a, b):
    """Mengembalikan hasil perkalian a * b"""
    return a * b

def divide(a, b):
    """Mengembalikan hasil pembagian a / b"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    """Mengembalikan hasil a pangkat b"""
    return a ** b