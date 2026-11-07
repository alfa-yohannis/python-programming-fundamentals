# Data harga produk
produk_harga = [
    {"nama": "Laptop", "harga": 9500000},
    {"nama": "Mouse", "harga": 150000},
    {"nama": "Keyboard", "harga": 350000},
    {"nama": "Monitor", "harga": 2200000}
]

# Data stok produk
produk_stok = [
    {"nama": "Laptop", "stok": 3},
    {"nama": "Mouse", "stok": 25},
    {"nama": "Keyboard", "stok": 10},
    {"nama": "Monitor", "stok": 4}
]


def gabung_dan_seleksi(produk_harga, produk_stok, batas_harga, batas_stok):
    """
    Menggabungkan dua struktur data berdasarkan nama produk
    dan menyeleksi produk dengan harga < batas_harga dan stok > batas_stok.
    """
    hasil = []

    for ph in produk_harga:
        for ps in produk_stok:
            if ph["nama"] == ps["nama"]:  # data produk sama
                if ph["harga"] < batas_harga and ps["stok"] > batas_stok:
                    gabung = {
                        "nama": ph["nama"],
                        "harga": ph["harga"],
                        "stok": ps["stok"]
                    }
                    hasil.append(gabung)
    return hasil


# Pemanggilan fungsi dengan kriteria tertentu
produk_terpilih = gabung_dan_seleksi(
    produk_harga, produk_stok, batas_harga=1000000, batas_stok=5
)

# Tampilkan hasil
print("Produk yang memenuhi kriteria:")
for p in produk_terpilih:
    print(p)
