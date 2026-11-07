# Perkalian Matriks Menggunakan List
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

C = [
    [0, 0],
    [0, 0]
]

for baris_a in range(0, len(A)):
    for kolom_b in range(0, len(B[0])):
        total = 0
        for i_pasangan in range(0, len(B)):
            total = total + A[baris_a][i_pasangan] * B[i_pasangan][kolom_b]
            print(f"{A[baris_a][i_pasangan]}*{B[i_pasangan][kolom_b]}", end=" ")
            if i_pasangan < len(B) - 1:
                print("+", end=" ")
        print(f"= {total}")
        C[baris_a][kolom_b] = total

print("Hasil akhir matriks C:")
for row in C:
    print(row)
