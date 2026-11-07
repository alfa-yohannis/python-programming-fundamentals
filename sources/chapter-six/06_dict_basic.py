# Dictionary
mahasiswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika"
}

print("Data awal:", mahasiswa)
print("Nama:", mahasiswa["nama"])

mahasiswa["umur"] = 21
mahasiswa["kota"] = "Tangerang"

del mahasiswa["jurusan"]

print("Setelah diubah:", mahasiswa)
