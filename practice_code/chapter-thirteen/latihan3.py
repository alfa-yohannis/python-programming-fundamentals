
stok = {"pensil": 10, "buku": 5, "pulpen": 8}

def tambah_stok(item, jumlah):
    if item in stok:
        stok[item] = stok[item] + jumlah    
    else:
        stok[item] = jumlah

def kurang_stok(item, jumlah):
    if item in stok and stok[item] - jumlah >= 0:
        stok[item] = stok[item] - jumlah
    else:
        stok[item] = 0     

def transaksi():
    keranjang = {"pensil": 3, "buku": 2}
    total = 0

    for item, qty in keranjang.items():
        kurang_stok(item, qty)
        total += qty

    return total

def main():
    print("Stok awal:", stok)
    transaksi()
    tambah_stok("pulpen", -3)   
    transaksi()
    print("Stok akhir:", stok)

if __name__ == "__main__":
    main()