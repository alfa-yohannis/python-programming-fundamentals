

def kelompokkan_penjualan(transaksi):

    data_per_bulan = dict.fromkeys(range(1, 13), [])

    for bulan, nilai in transaksi:
        if bulan in data_per_bulan:
            data_per_bulan[bulan].append(nilai)
        else:
            data_per_bulan[bulan] = [nilai]

    return data_per_bulan

def hitung_total_per_bulan(data_per_bulan):
    total = {}
    for bulan, daftar_nilai in data_per_bulan.items():
        total[bulan] = sum(daftar_nilai)
    return total

def main():
    transaksi = [
        (1, 100_000),
        (1, 150_000),
        (2, 200_000),
        (3, 50_000),
        (3, 75_000),
        (12, 300_000),
    ]

    data_per_bulan = kelompokkan_penjualan(transaksi)
    print("Data per bulan:", data_per_bulan)

    total = hitung_total_per_bulan(data_per_bulan)
    print("Total per bulan:", total)

if __name__ == "__main__":
    main()