usia = 25
punya_surat_izin_mengemudi = True

if usia >= 18:  # Kondisi luar: cek apakah usia sudah 18 tahun ke atas
    print("Kamu sudah dewasa.")
    if punya_surat_izin_mengemudi:  # Kondisi dalam: cek apakah sudah punya SIM
        print("Kamu boleh mengemudi.")
    else:
        print("Kamu sudah dewasa, tapi belum punya SIM.")
else:
    print("Kamu belum dewasa.")
