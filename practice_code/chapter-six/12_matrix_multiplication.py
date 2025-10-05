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

for i in range(0, len(A)):
    for j in range(0, len(B[0])):
        total = 0
        for k in range(0, len(B)):
            total = total + A[i][k] * B[k][j]
            print(f"{A[i][k]}*{B[k][j]}", end=" ")
            if k < len(B) - 1:
                print("+", end=" ")
        print(f"= {total}")
        C[i][j] = total

print("Hasil akhir matriks C:")
for row in C:
    print(row)
