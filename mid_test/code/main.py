# main.py
"""
app/main.py — Titik Masuk Utama Aplikasi Flash Card

Modul ini berfungsi sebagai **antarmuka utama (entry point)** dari aplikasi Flash Card App.
Ketika dijalankan, modul ini menampilkan menu utama berbasis terminal yang memungkinkan
pengguna memilih antara dua mode pembelajaran interaktif:
1. **Exercises (Latihan)** — Mode latihan tanpa penilaian.
2. **Quiz (Kuis)** — Mode kuis pilihan ganda dengan pencatatan hasil.

Fungsi Utama
------------
- `main()`:
    Menampilkan menu utama, menerima input pengguna, dan mengarahkan eksekusi
    ke fungsi yang sesuai berdasarkan pilihan pengguna.
    Fungsi ini berjalan dalam loop hingga pengguna memilih untuk keluar dari aplikasi.

Konstanta Identitas
-------------------
- `STUDENT_ID`   : Digunakan untuk mencatat atau mengidentifikasi pengguna aplikasi.
                   Nilai awal berupa placeholder yang dapat diubah sesuai identitas mahasiswa.
- `STUDENT_NAME` : Nama lengkap pengguna (mahasiswa) yang menjalankan aplikasi.

Fitur Menu
----------
1. **Exercises** — Menjalankan fungsi `run_exercises()` dari modul `app.exercises`.
   Pengguna dapat berlatih memahami konsep Python menggunakan flashcard,
   dengan opsi menampilkan atau menyembunyikan jawaban.

2. **Quiz** — Menjalankan fungsi `show_quiz()` dari modul `app.quiz`.
   Pengguna menjawab pertanyaan pilihan ganda, dan hasilnya akan dicatat ke file CSV.

3. **Exit** — Keluar dari aplikasi dengan pesan perpisahan.

Dependensi Internal
-------------------
- `run_exercises` : Fungsi utama dari `app.exercises` untuk mode latihan.
- `show_quiz`     : Fungsi utama dari `app.quiz` untuk mode kuis interaktif.
- `clear_console` : Utilitas dari `app.utils` untuk membersihkan tampilan terminal.

Alur Eksekusi
-------------
1. Aplikasi dijalankan melalui:
       $ python main.py
2. Program memanggil fungsi `main()` yang menampilkan menu utama.
3. Berdasarkan input pengguna:
       - Pilihan 1 → memanggil `run_exercises()`
       - Pilihan 2 → memanggil `show_quiz()`
       - Pilihan 3 → keluar dari aplikasi
4. Loop utama berlanjut hingga pengguna memilih keluar.

Struktur Menu
--------------
    === Flash Card App ===
    1. Exercises
    2. Quiz
    3. Exit

Pengujian & Integrasi
---------------------
- Modul ini diujikan dengan menggunakan `pytest` melalui simulasi input (`monkeypatch`).
- Fungsi `clear_console()` dapat di-patch agar tidak membersihkan terminal selama pengujian.

Catatan
--------
- Modul ini **tidak dimaksudkan untuk diimpor** oleh modul lain, tetapi untuk dijalankan langsung.
- Ketika file ini dijalankan secara langsung (bukan diimpor), Python akan mengeksekusi blok:
      if __name__ == "__main__":
          main()
  yang memulai antarmuka menu utama.

Contoh Eksekusi
---------------
    $ python main.py
    === Flash Card App ===
    1. Exercises
    2. Quiz
    3. Exit
    Choose an option (1-3): 1
    (Menjalankan mode latihan interaktif)

    $ python main.py
    === Flash Card App ===
    1. Exercises
    2. Quiz
    3. Exit
    Choose an option (1-3): 3
    Exiting the app. Goodbye.

Lisensi & Tujuan
----------------
- Modul ini dikembangkan untuk keperluan edukasi, khususnya dalam konteks
  pembelajaran dasar-dasar Python di lingkungan akademik seperti Pradita University.
"""

from app.exercises import run_exercises
from app.quiz import show_quiz
from app.utils import clear_console


STUDENT_ID = "00000000"
STUDENT_NAME = "Alice"

def main():
    """
    Menjalankan menu utama aplikasi Flash Card App.

    Tujuan:
        Fungsi ini merupakan titik masuk utama (entry point) aplikasi berbasis terminal
        yang menyediakan tiga opsi utama kepada pengguna:
        1. Latihan (Exercises)
        2. Kuis (Quiz)
        3. Keluar dari aplikasi

    Proses:
        1) Membersihkan layar terminal menggunakan `clear_console()`.
        2) Menampilkan menu utama dengan tiga pilihan numerik.
        3) Menerima input pengguna melalui `input()`.
        4) Menjalankan aksi berdasarkan pilihan pengguna:
            - "1" → Menjalankan sesi latihan interaktif (`run_exercises()`).
            - "2" → Menjalankan sesi kuis pilihan ganda (`show_quiz()`).
            - "3" → Menampilkan pesan keluar dan mengakhiri program.
            - Input lain → Menampilkan pesan kesalahan dan meminta pengguna mengulang.

    Interaksi Pengguna:
        Input:
            - 1 → Mode latihan
            - 2 → Mode kuis
            - 3 → Keluar
        Output:
            - Tampilan menu utama dan pesan status setiap kali fungsi dijalankan.

    Ketergantungan internal:
        - `clear_console()` : Membersihkan tampilan terminal setiap kali menu dimuat ulang.
        - `run_exercises()` : Menjalankan mode latihan flashcard.
        - `show_quiz()`     : Menjalankan mode kuis interaktif.

    Nilai Kembalian:
        None — Fungsi ini berjalan secara berulang (looping) hingga pengguna memilih keluar.

    Alur Pemanggilan Fungsi:
        main()
          ├─▶ clear_console()
          ├─▶ run_exercises() (jika pilih 1)
          ├─▶ show_quiz()     (jika pilih 2)
          └─▶ break            (jika pilih 3)

    Catatan:
        - Fungsi ini hanya cocok dijalankan pada lingkungan terminal interaktif.
        - Untuk pengujian otomatis, input pengguna dapat disimulasikan menggunakan `monkeypatch`.

    Contoh Penggunaan:
        >>> main()
        === Flash Card App ===
        1. Exercises
        2. Quiz
        3. Exit
        Choose an option (1-3): 1
        (Menjalankan mode latihan)
    """
    while True:
        clear_console()
        print("=== Flash Card App ===")
        print("1. Exercises")
        print("2. Quiz")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            run_exercises()
        elif choice == "2":
            show_quiz()
        elif choice == "3":
            clear_console()
            print("Exiting the app. Goodbye.")
            break
        else:
            print("\nInvalid option. Please choose between 1 and 3.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    """
    Titik masuk utama (entry point) program Flash Card App.

    Saat file ini dijalankan secara langsung (bukan diimpor sebagai modul),
    blok ini akan memanggil fungsi `main()` untuk memulai antarmuka menu utama aplikasi.

    Fungsi `main()` akan terus berjalan dalam loop hingga pengguna memilih untuk keluar.

    Contoh:
        $ python main.py
        === Flash Card App ===
        1. Exercises
        2. Quiz
        3. Exit
        Choose an option (1-3): 2
        (Menjalankan kuis interaktif)
    """
    main()
