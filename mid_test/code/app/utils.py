"""
app/utils.py

Modul ini menyediakan fungsi utilitas umum yang digunakan di berbagai bagian aplikasi,
terutama untuk mendukung tampilan terminal dan interaksi konsol.

Fungsi utama yang disediakan:
    - clear_console(): Membersihkan layar konsol pada berbagai sistem operasi.

Modul ini digunakan oleh modul lain seperti:
    - app/quiz.py atau app/tests.py, khususnya saat menjalankan sesi latihan atau kuis.
"""

import os


def clear_console():
    """
    Membersihkan layar konsol pada semua platform (Windows, Linux, dan MacOS).

    Tujuan:
        Fungsi ini digunakan untuk menjaga tampilan terminal tetap bersih dan fokus
        saat pengguna berpindah dari satu pertanyaan ke pertanyaan berikutnya,
        atau sebelum menampilkan ringkasan hasil kuis.

    Parameter:
        (tidak memiliki parameter)

    Nilai Kembalian:
        int:
            Kode status hasil eksekusi perintah sistem.
            - `0` umumnya menunjukkan perintah berhasil dijalankan.
            - Nilai lain (non-zero) menunjukkan adanya kegagalan atau peringatan.

    Proses:
        1. Mengecek sistem operasi menggunakan `os.name`:
            - `'nt'` → berarti sistem Windows.
            - Lainnya (`'posix'`, dsb.) → berarti Linux atau MacOS.
        2. Menentukan perintah terminal yang sesuai:
            - `'cls'` untuk Windows.
            - `'clear'` untuk Linux/Mac.
        3. Menjalankan perintah tersebut menggunakan `os.system(cmd)`.
        4. Mengembalikan hasil eksekusi (kode status).

    Kapan dan di mana fungsi ini dipanggil:
        Fungsi ini dipanggil di berbagai bagian aplikasi interaktif, khususnya:
        - Di dalam `_ask()` → sebelum menampilkan pertanyaan baru kepada pengguna.
        - Di dalam `show_quiz()` → saat membersihkan layar sebelum menampilkan hasil akhir.
        - Di dalam menu utama (`main.py`) → ketika berpindah antara mode.

    Alur Pemanggilan Fungsi (Contoh dalam konteks kuis):
        show_quiz()
            ├─▶ _ask()
            │     ├─▶ clear_console()   ← sebelum menampilkan pertanyaan
            │     └─▶ input()           ← menunggu jawaban pengguna
            └─▶ clear_console()         ← sebelum menampilkan ringkasan hasil

    Contoh Penggunaan:
        >>> from app.utils import clear_console
        >>> clear_console()
        0  # (jika berhasil)

    Catatan:
        - Fungsi ini hanya bekerja di lingkungan terminal (console).
        - Dalam konteks pengujian otomatis (pytest), fungsi ini biasanya dimonkeypatch
          agar tidak benar-benar membersihkan terminal.
    """
    cmd = "cls" if os.name == "nt" else "clear"
    result = os.system(cmd)
    return result
