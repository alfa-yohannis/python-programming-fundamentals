def hitung_diskon(harga, diskon):
    hasil = harga - harga * diskon  # Logika salah (diskon seharusnya persentase)
    return hasil

total = hitung_diskon(100000, 20)  # Maksudnya 20% tapi ditulis 20
print("X")
print("Total harga:", total)