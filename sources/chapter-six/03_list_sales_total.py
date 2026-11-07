# Menghitung Total Penjualan Harian
penjualan = [120000, 85000, 95000, 110000, 130000]

total = 0
for p in penjualan:
    total += p

print("Total penjualan minggu ini:", f"Rp{total:,}")
