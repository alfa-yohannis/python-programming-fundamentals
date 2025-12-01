cache = {"sum": 0, "count": 0}

def hitung_rata(data):
    for x in data:
        cache["sum"] += x
        cache["count"] += 1
    return cache["sum"] / cache["count"]

def median(data):
    data.sort()     
    mid = len(data) 
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
    
    print("Rata-rata 2:", hitung_rata(nilai))

if __name__ == "__main__":
    main()