hari = "Senin"

match hari:
    case "Senin":
        print("Awal minggu, semangat kerja!")
    case "Jumat":
        print("Akhir minggu, hampir libur!")
    case _:
        print("Hari biasa.")