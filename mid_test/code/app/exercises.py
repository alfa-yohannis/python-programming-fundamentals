# app/exercises.py
"""
app/exercises.py — Modul Latihan Flashcard (Python 101)

Modul ini menyediakan fitur latihan interaktif berbasis flashcard untuk membantu pengguna
mempelajari konsep Python secara mandiri. Tidak seperti mode kuis (`quiz.py`) yang menilai jawaban,
mode latihan ini hanya menampilkan pertanyaan dan jawaban tanpa penilaian benar/salah.

Fitur Utama
-----------
1) Memuat daftar flashcard dari file CSV yang berisi pertanyaan dan jawaban.
2) Menampilkan satu pertanyaan per langkah dengan opsi untuk:
   - Menampilkan/menyembunyikan jawaban.
   - Melanjutkan ke pertanyaan berikutnya.
   - Kembali ke menu utama.
3) Mengacak urutan pertanyaan setiap kali seluruh daftar telah ditampilkan.
4) Menampilkan antarmuka terminal yang sederhana dan ramah pengguna.

Dependensi
----------
- Standar Python: csv, os, random
- Modul lokal: app.utils.clear_console

Struktur Data & File
--------------------
- Sumber data utama: data/flashcards/python.csv
- Format file yang diharapkan:
    Header: id, question, answer
    Contoh isi:
        id,question,answer
        1,"Apa itu Python?","Bahasa pemrograman"
        2,"Simbol penugasan di Python?","="

- Data setiap baris akan dimuat ke dalam list[dict] dengan format:
    {"question": "...", "answer": "..."}

Konstanta
---------
- DATA_FILE:
    Path absolut menuju file sumber flashcard.
    Nilai default: data/flashcards/python.csv

Fungsi Utama
------------
- _load_flashcards():
    Membaca data flashcard dari CSV dan mengembalikannya dalam bentuk list[dict].
    Jika file tidak ditemukan, fungsi mengembalikan list kosong agar program tetap berjalan.

- run_exercises():
    Menjalankan sesi latihan interaktif.
    Pengguna dapat menampilkan/menyembunyikan jawaban, berpindah antar soal, atau keluar.
    Urutan soal diacak setiap kali semua pertanyaan selesai ditampilkan.

Alur Eksekusi
-------------
main() ─▶ run_exercises()
          └─▶ _load_flashcards()
               └─▶ (loop latihan: tampilkan pertanyaan → toggle jawaban → lanjut/back)

Perilaku & I/O
--------------
- Aplikasi berjalan di terminal dan menggunakan input/output berbasis teks:
    Input:  S (show/hide), N (next), B (back)
    Output: pertanyaan, jawaban, dan instruksi
- Fungsi clear_console() dipanggil untuk membersihkan layar di setiap iterasi tampilan.

Catatan Pengujian
-----------------
- Untuk pengujian otomatis dengan pytest:
    - Gunakan monkeypatch untuk mengganti `input()` agar dapat disimulasikan.
    - Patch `clear_console()` agar tidak benar-benar membersihkan layar.
    - Arahkan DATA_FILE ke file sementara di direktori tmp_path untuk pengujian isolasi.

Lisensi & Tujuan
----------------
- Dirancang untuk mendukung pembelajaran interaktif Python 101 di lingkungan akademik
  (misalnya, Pradita University).
- Kode ini sederhana dan mudah diperluas untuk materi atau dataset baru.
"""

import csv
import os
import random
from app.utils import clear_console

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data/flashcards", "python.csv")

def _load_flashcards():
    """
    Memuat (membaca) flashcard dari file data CSV ke dalam struktur data Python.

    Tujuan:
        Fungsi ini digunakan untuk membaca seluruh daftar pertanyaan dan jawaban
        dari berkas sumber (CSV) agar dapat digunakan pada sesi kuis atau latihan interaktif.

    Lokasi File:
        File yang dimuat ditentukan oleh variabel global `DATA_FILE`, dengan path default:
            data/flashcards/python.csv

    Format File yang Diharapkan:
        - Header: id, question, answer
        - Setiap baris berisi teks pertanyaan dan jawaban.
        - Hanya baris yang memiliki nilai `question` dan `answer` yang tidak kosong akan dimasukkan.
        Contoh isi file:
            id,question,answer
            1,"Apa itu Python?","Bahasa pemrograman"
            2,"Simbol penugasan di Python?","="

    Proses:
        1. Membuka file CSV menggunakan `csv.DictReader` untuk membaca data berbasis header.
        2. Melakukan pembersihan spasi dengan `.strip()` pada setiap nilai kolom `question` dan `answer`.
        3. Menyimpan setiap baris valid ke dalam list dalam bentuk:
               {"question": "...", "answer": "..."}
        4. Jika file tidak ditemukan (`FileNotFoundError`), fungsi akan **mengembalikan list kosong**
           agar aplikasi tidak gagal dan tetap dapat berjalan.

    Parameter:
        (tidak memiliki parameter)

    Nilai Kembalian:
        list[dict]:
            Daftar berisi pasangan pertanyaan dan jawaban.
            Contoh hasil:
                [
                    {"question": "Apa itu Python?", "answer": "Bahasa pemrograman"},
                    {"question": "Simbol penugasan di Python?", "answer": "="}
                ]

    Kapan dan di mana fungsi ini dipanggil:
        - Fungsi ini dipanggil **di awal proses kuis** oleh `show_quiz()` untuk menyiapkan
          kumpulan pertanyaan yang akan ditampilkan secara acak kepada pengguna.
        - Dapat juga digunakan oleh modul lain (misalnya `exercises.py`) yang membutuhkan
          data flashcard dalam format list.

    Alur Pemanggilan Fungsi:
        show_quiz() ─▶ _load_flashcards()

    Contoh Penggunaan:
        >>> cards = _load_flashcards()
        >>> len(cards)
        10
        >>> cards[0]
        {'question': 'Apa itu Python?', 'answer': 'Bahasa pemrograman'}

    Catatan:
        - Jika file CSV tidak ditemukan, fungsi ini tidak akan menimbulkan error.
          Hal ini memungkinkan aplikasi menampilkan pesan ramah seperti “No flashcards found.”
        - File CSV harus disimpan dalam format UTF-8 agar pembacaan karakter non-ASCII berhasil.
    """
    cards = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = (row.get("question") or "").strip()
                a = (row.get("answer") or "").strip()
                if q and a:
                    cards.append({"question": q, "answer": a})
    except FileNotFoundError:
        pass
    return cards


def run_exercises():
    """
    Menjalankan sesi latihan flashcard secara interaktif (tanpa menu).

    Tujuan:
        Memberikan mode latihan berbasis flashcard di mana pengguna dapat
        melihat pertanyaan, menampilkan/menyembunyikan jawaban, lalu berpindah
        ke soal berikutnya dalam urutan acak yang terus diacak ulang ketika
        semua soal telah dilalui.

    Proses:
        1) Memanggil `_load_flashcards()` untuk memuat seluruh soal-jawaban.
           - Jika tidak ada data, tampilkan informasi dan kembali.
        2) Membuat urutan indeks acak (`order`) dari seluruh kartu.
        3) Menampilkan satu kartu pada satu waktu:
           - Tampilkan pertanyaan.
           - Jawaban disembunyikan secara default, dapat ditoggle (S).
           - Pindah ke kartu berikutnya (N).
           - Kembali/keluar dari latihan (B).
        4) Saat seluruh kartu selesai ditampilkan, urutan akan diacak ulang
           dan siklus latihan berulang dari awal.

    Interaksi Pengguna:
        - [S] Show/Hide: menampilkan atau menyembunyikan jawaban.
        - [N] Next     : berpindah ke soal berikutnya.
        - [B] Back     : keluar dari mode latihan (kembali ke pemanggil).

    Parameter:
        (tidak ada)

    Nilai Kembalian:
        None — fungsi ini bersifat prosedural dan berinteraksi melalui terminal.

    Kapan dan di mana fungsi ini dipanggil:
        - Dipanggil dari antarmuka utama aplikasi (mis. `main.py`) saat pengguna
          memilih mode Latihan (Exercises).

    Ketergantungan internal:
        - `_load_flashcards()` untuk memuat data.
        - `clear_console()` untuk merapikan tampilan antar-langkah.
        - `random.shuffle()` untuk mengacak urutan soal.

    Alur Pemanggilan Fungsi:
        main() ─▶ run_exercises()
                    └─▶ _load_flashcards()
                         └─▶ (loop latihan: tampilkan soal → toggle jawaban → berikutnya)

    Catatan:
        - Untuk pengujian otomatis (pytest), interaksi `input()` dapat disimulasikan
          menggunakan monkeypatch; `clear_console()` biasanya dipatch agar tidak
          benar-benar membersihkan terminal saat tes berjalan.
    """
    cards = _load_flashcards()
    if not cards:
        clear_console()
        print("No flashcards found.")
        print(f"Expected: {os.path.abspath(DATA_FILE)}")
        input("\nPress Enter to go back...")
        return

    # Urutan acak yang diacak ulang ketika habis
    order = list(range(len(cards)))
    random.shuffle(order)
    ptr = 0

    while True:
        if ptr >= len(order):
            random.shuffle(order)
            ptr = 0

        current = cards[order[ptr]]
        shown = False

        while True:
            clear_console()
            print("Exercise (Python 101)\n")
            print("Q:", current["question"])
            print("\nA:", current["answer"] if shown else "(hidden)")
            print("\n[S] Show/Hide   [N] Next   [B] Back")

            choice = input("\nChoose (S/N/B): ").strip().lower()
            if choice == "s":
                shown = not shown
            elif choice == "n":
                ptr += 1
                break
            elif choice == "b":
                return
            else:
                print("Invalid option.")
                input("\nPress Enter to continue...")
