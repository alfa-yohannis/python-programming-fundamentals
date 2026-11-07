# Set
angka = {1, 2, 3, 3, 2}
print("Data awal:", angka)

angka.add(4)
angka.add(5)
angka.discard(2)

print("Setelah diubah:", angka)

angka_lain = {3, 4, 6}
print("Gabungan:", angka | angka_lain)
print("Irisan:", angka & angka_lain)
