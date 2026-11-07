# Daftar nilai ujian
nilai_ujian = [78, 85, 90, 67, 88, 92, 74, 90, 81]


def cari_nilai_tertinggi(data):
    """Mengembalikan nilai tertinggi dari list menggunakan looping."""
    tertinggi = data[0]
    for n in data:
        if n > tertinggi:
            tertinggi = n
    return tertinggi


def cari_nilai_terendah(data):
    """Mengembalikan nilai terendah dari list menggunakan looping."""
    terendah = data[0]
    for n in data:
        if n < terendah:
            terendah = n
    return terendah


def cek_nilai(data, target):
    """Memeriksa apakah nilai tertentu ada dalam list."""
    for n in data:
        if n == target:
            return True
    return False


# Pemanggilan fungsi
nilai_dicari = 90
nilai_tertinggi = cari_nilai_tertinggi(nilai_ujian)
nilai_terendah = cari_nilai_terendah(nilai_ujian)
ada_nilai = cek_nilai(nilai_ujian, nilai_dicari)

# Tampilkan hasil
print("Daftar nilai ujian:", nilai_ujian)
print("Nilai tertinggi :", nilai_tertinggi)
print("Nilai terendah  :", nilai_terendah)

if ada_nilai:
    print(f"Nilai {nilai_dicari} ditemukan dalam daftar.")
else:
    print(f"Nilai {nilai_dicari} tidak ditemukan.")
