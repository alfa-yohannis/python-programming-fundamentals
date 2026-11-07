# Mencetak angka ganjil dari 1 sampai 10
for i in range(1, 11):
    if i % 2 == 0: # Jika angka genap
        continue   # Lewati iterasi ini dan lanjut ke angka berikutnya
    print(f"Angka ganjil: {i}")