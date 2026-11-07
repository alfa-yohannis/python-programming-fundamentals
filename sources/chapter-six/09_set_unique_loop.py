# Data Unik dengan Set
produk = {"kopi", "teh", "gula", "kopi", "susu"}

print("Daftar produk unik:")
for p in produk:
    print("-", p)

# tambahkan elemen baru
produk.add("keju")
print("\nSetelah ditambah:")
for p in produk:
    print("-", p)
