# Latihan 1: Shared mutable state menyebabkan hasil salah
cache = {"sum": 0, "count": 0}

def hitung_rata(data):
    for x in data:
        cache["sum"] += x
        cache["count"] += 1
    return cache["sum"] / cache["count"]

def median(data):
    data.sort()        # Memodifikasi list asli
    mid = len(data) // 2
    return data[mid]

def modus(data):
    frekuensi = {}
    for x in data:
        frekuensi[x] = frekuensi.get(x, 0) + 1
    sorted_items = sorted(frekuensi.items(), key=lambda y: y[1])
    return sorted_items[-1][0]

def main():
    nilai = [70, 80, 80, 90, 100]
    print("Rata-rata:", hitung_rata(nilai))
    print("Median:", median(nilai))
    print("Modus:", modus(nilai))
    
    nilai.append(80.5)

    # Panggilan ulang (bug makin jelas)
    print("Rata-rata 2:", hitung_rata(nilai))
    print("Median 2:", median(nilai))
    print("Modus 2:", modus(nilai))
    
    # nilai.append(80)

    # # Panggilan ulang (bug makin jelas)
    # print("Rata-rata 3:", hitung_rata(nilai))
    # print("Median 3:", median(nilai))
    # print("Modus 3:", modus(nilai))

if __name__ == "__main__":
    main()