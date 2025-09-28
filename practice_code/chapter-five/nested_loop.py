# Outer loop untuk baris
for i in range(1, 4):  # Baris 1 sampai 3
    # Inner loop untuk kolom
    for j in range(1, 4): # Kolom 1 sampai 3
        print(f"{i}x{j} = {i*j}", end='\t')
    print() # Pindah ke baris baru setelah inner loop selesai