# Titik-titik sudut kubus (dalam koordinat 3D)
titik_kubus = [
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
    (0, 1, 1)
]


def hitung_pusat_massa(titik_list):
    """Menghitung koordinat pusat massa dari list titik 3D."""
    jumlah_x = 0
    jumlah_y = 0
    jumlah_z = 0

    for x, y, z in titik_list:
        jumlah_x += x
        jumlah_y += y
        jumlah_z += z

    n = len(titik_list)
    return (jumlah_x / n, jumlah_y / n, jumlah_z / n)


# Pemanggilan fungsi
pusat_massa = hitung_pusat_massa(titik_kubus)

# Tampilkan hasil
print("Koordinat titik-titik kubus:")
for titik in titik_kubus:
    print(titik)

print("\nPusat massa kubus:", pusat_massa)
