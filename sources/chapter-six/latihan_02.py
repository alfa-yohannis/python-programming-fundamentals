# Daftar nilai ujian
nilai = [85, 90, 78, 92, 88, 75, 95]


def urutkan_ascending(data):
    """Urutkan dari kecil ke besar dengan pendekatan manusiawi."""
    hasil = []
    sumber = data[:]  # salin agar data asli tidak berubah

    while sumber:
        # cari nilai terkecil secara manual
        terkecil = sumber[0]
        for n in sumber:
            if n < terkecil:
                terkecil = n
        hasil.append(terkecil)
        sumber.remove(terkecil)
    return hasil


def urutkan_descending(data):
    """Urutkan dari besar ke kecil dengan pendekatan manusiawi."""
    hasil = []
    sumber = data[:]  # salin agar data asli tidak berubah

    while sumber:
        # cari nilai terbesar secara manual
        terbesar = sumber[0]
        for n in sumber:
            if n > terbesar:
                terbesar = n
        hasil.append(terbesar)
        sumber.remove(terbesar)
    return hasil


# Pemanggilan fungsi
urut_ascending = urutkan_ascending(nilai)
urut_descending = urutkan_descending(nilai)

# Tampilkan hasil
print("Data asli       :", nilai)
print("Urut Ascending  :", urut_ascending)
print("Urut Descending :", urut_descending)
