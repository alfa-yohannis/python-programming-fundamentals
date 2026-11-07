# Data pelanggan dari dua cabang toko
cabang_a = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
cabang_b = {"Budi", "Dewi", "Farah", "Gilang", "Hadi"}


def analisis_pelanggan(cabang_a, cabang_b):
    """
    Melakukan berbagai operasi himpunan untuk menganalisis
    kesamaan dan perbedaan pelanggan antar dua cabang.
    """
    hasil = {}

    # Irisan (pelanggan di kedua cabang)
    hasil["and"] = cabang_a & cabang_b

    # Gabungan (semua pelanggan tanpa duplikasi)
    hasil["or"] = cabang_a | cabang_b

    # Selisih (pelanggan hanya di cabang B)
    hasil["not_in_a"] = cabang_b - cabang_a

    # Selisih simetris (pelanggan hanya di salah satu cabang)
    hasil["xor"] = cabang_a ^ cabang_b

    return hasil


# Pemanggilan fungsi
hasil = analisis_pelanggan(cabang_a, cabang_b)

# Tampilkan hasil analisis
print("Pelanggan di kedua cabang (AND):", hasil["and"])
print("Gabungan pelanggan (OR):", hasil["or"])
print("Pelanggan hanya di cabang B (NOT IN A):", hasil["not_in_a"])
print("Pelanggan hanya di salah satu cabang (XOR):", hasil["xor"])
