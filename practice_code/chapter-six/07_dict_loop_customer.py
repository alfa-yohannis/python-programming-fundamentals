# Menampilkan Data Pelanggan
pelanggan = {
    "nama": "Sinta Dewi",
    "usia": 28,
    "kota": "Tangerang"
}

print("Data Pelanggan:")

for k, v in pelanggan.items():
    print(f"{k.capitalize():<6}: {v}")

# ubah data
pelanggan["usia"] = 29
print("\nUsia diperbarui:", pelanggan["usia"])
