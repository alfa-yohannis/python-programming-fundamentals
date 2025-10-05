# Mengolah Data Bersarang dengan Perulangan dan Kondisi
mahasiswa = [
    {"nama": "Andi", "nilai": [80, 85, 90]},
    {"nama": "Budi", "nilai": [60, 70, 65]},
    {"nama": "Citra", "nilai": [90, 95, 100]}
]

for m in mahasiswa:
    total = 0
    for n in m["nilai"]:
        total += n

    rata = total / len(m["nilai"])
    
    if rata >= 85:
        kategori = "Sangat Baik"
    elif rata >= 70:
        kategori = "Cukup"
    else:
        kategori = "Perlu Perbaikan"
    
    print(f"{m['nama']} - Rata-rata: {rata:.1f} ({kategori})")
