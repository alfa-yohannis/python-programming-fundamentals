# Contoh penggunaan breakpoint() untuk debugging
angka = [10, 20, 30, 40]
total = 0

for x in angka:
    breakpoint()   # Masuk ke mode debugger di setiap iterasi
    total += x
    print("Total sementara:", total)

print("Total akhir:", total)