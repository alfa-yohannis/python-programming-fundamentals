# 🧠 Ujian Tengah Semester (UTS): Flash Card App — Console Application Implementation

## 🎯 Tujuan Pembelajaran
Latihan ini dirancang untuk melatih Anda mengimplementasikan ulang fungsi-fungsi utama dalam aplikasi **Flash Card App** untuk aplikasi terminal/console.

Tujuan pembelajaran:
- Memahami struktur proyek Python modular.
- Menulis fungsi sesuai spesifikasi dan antarmuka (API).
- Menggunakan **pytest** untuk memverifikasi kebenaran kode. **pytest** adalah tool otomatis untuk melakukan test terhadap kode yang dibuat berdasarkan spesifikasi kode pengujian yang dibuat.
- Mengelola file CSV dan interaksi konsol sederhana.
- Penggunaan perulangan, pengkondisian, tipe data, dan variabel.

---

## 📁 Struktur Proyek

```
project_root/
│
├── app/
│   ├── __init__.py
│   ├── utils.py
│   ├── exercises.py
│   └── quiz.py
│
├── data/
│   ├── flashcards/python.csv
│   └── results/
│
├── tests/
│   ├── conftest.py
│   ├── test_*.py
│
├── main.py
└── pytest.ini
```

---

## ⚙️ Perilaku Aplikasi Flash Card App

Aplikasi **Flash Card App** adalah aplikasi terminal berbasis Python yang digunakan untuk membantu pengguna mempelajari konsep dasar pemrograman (khususnya Python) melalui dua mode utama: **Latihan (Exercises)** dan **Kuis (Quiz)**.  
Aplikasi ini bekerja sepenuhnya melalui antarmuka teks (console/terminal) tanpa GUI, dan semua interaksi dilakukan menggunakan perintah `input()` serta `print()`.

### 🧭 Alur Umum Aplikasi

1. **Menampilkan Menu Utama**  
   Saat dijalankan, aplikasi akan menampilkan menu utama dengan tiga pilihan:
   - `1` → Mode latihan flashcard (Exercises)  
   - `2` → Mode kuis pilihan ganda (Quiz)  
   - `3` → Keluar dari aplikasi  
   Pemilihan menu dilakukan dengan memasukkan angka sesuai opsi.  

2. **Mode Latihan (Exercises)**  
   Pada mode ini, pengguna dapat berlatih secara interaktif dengan melihat pertanyaan satu per satu.  
   Jawaban dapat ditampilkan atau disembunyikan dengan menekan tombol:
   - `S` → Menampilkan atau menyembunyikan jawaban.  
   - `N` → Pindah ke soal berikutnya.  
   - `B` → Kembali ke menu utama.  
   Pertanyaan ditampilkan dalam urutan acak yang terus diacak ulang setiap kali semua kartu telah habis ditampilkan.

3. **Mode Kuis (Quiz)**  
   Dalam mode ini, pengguna akan mendapatkan beberapa pertanyaan pilihan ganda (default: 5 soal acak).  
   - Tiap soal menampilkan tiga opsi jawaban (1 benar + 2 pengecoh).  
   - Pengguna menjawab dengan menekan `A/B/C` atau `1/2/3`.  
   - Mengetik `Q` atau `quit` akan menghentikan kuis di tengah jalan.  
   Setelah selesai, aplikasi akan menampilkan ringkasan skor dan menyimpannya ke file hasil.

4. **Penyimpanan Data**  
   - Flashcards dibaca dari file `data/flashcards/python.csv`.  
   - Hasil kuis disimpan ke `data/results/results.csv`.  
   - Jika file atau direktori belum ada, sistem akan otomatis membuatnya agar struktur data tetap konsisten.

---

## 📂 Perilaku Spesifik per Modul

### 🧩 `main.py`
- **Peran:** Titik masuk utama aplikasi.  
- **Perilaku:**  
  - Menampilkan menu utama dan mengatur navigasi antar-mode.  
  - Memanggil fungsi `run_exercises()` (latihan) atau `show_quiz()` (kuis).  
  - Menggunakan `clear_console()` untuk membersihkan tampilan setiap kali menu dimuat ulang.  
  - Berhenti ketika pengguna memilih “Exit” (opsi 3).  

---

### 🧠 `app/exercises.py`
- **Peran:** Menyediakan mode latihan berbasis flashcard.  
- **Fungsi utama:**  
  - `_load_flashcards()`  
    Membaca file CSV berisi pertanyaan dan jawaban. Jika file tidak ada, mengembalikan list kosong agar aplikasi tidak gagal.  
  - `run_exercises()`  
    Mengatur seluruh sesi latihan interaktif — menampilkan pertanyaan satu per satu, menampilkan jawaban jika diminta, dan mengizinkan pengguna berpindah ke pertanyaan berikutnya.  
- **Perilaku penting:**  
  - Urutan pertanyaan selalu diacak menggunakan `random.shuffle()`.  
  - Ketika semua pertanyaan selesai ditampilkan, urutan diacak ulang untuk sesi berikutnya.  
  - Input tidak valid akan menampilkan pesan kesalahan tanpa menghentikan aplikasi.  

---

### 🧮 `app/quiz.py`
- **Peran:** Menjalankan mode kuis pilihan ganda dengan sistem penilaian otomatis.  
- **Fungsi utama dan perilakunya:**  

  #### `_load_flashcards()`
  - Membaca semua pertanyaan dan jawaban dari `data/flashcards/python.csv`.  
  - Mengabaikan baris kosong atau data tidak lengkap.  
  - Mengembalikan list berisi dict dengan kunci `"question"` dan `"answer"`.

  #### `_build_options()`
  - Membentuk daftar pilihan jawaban acak (default 3 opsi).  
  - Selalu memastikan ada satu jawaban benar dan dua pengecoh.  
  - Jika jumlah data terlalu sedikit, akan menggandakan opsi agar jumlah tetap 3.  

  #### `_ask()`
  - Menampilkan satu pertanyaan beserta tiga opsi jawaban.  
  - Menunggu input pengguna (`A/B/C` atau `1/2/3`) untuk memilih jawaban.  
  - Menangani keluar di tengah kuis dengan `Q` atau `quit`.  
  - Memberikan umpan balik langsung (“Correct!” atau “Incorrect.”).  

  #### `_save_result()` dan `_ensure_results_header()`
  - Menjamin file hasil (`data/results/results.csv`) selalu memiliki header standar.  
  - Menyimpan setiap hasil kuis dalam format CSV dengan:
    ```
    timestamp, total_questions, correct, percentage
    ```
  - Jika file belum ada, akan otomatis dibuat.  

  #### `show_quiz()`
  - Mengatur seluruh alur kuis dari awal hingga akhir:
    1. Memuat data flashcard.
    2. Menentukan pertanyaan acak.
    3. Menampilkan soal dan menerima jawaban.
    4. Menghitung skor akhir.
    5. Menyimpan hasil ke file CSV.
  - Jika tidak ada data, menampilkan pesan error yang ramah dan kembali ke menu utama.

---

### 🧼 `app/utils.py`
- **Peran:** Menyediakan fungsi utilitas umum.  
- **Fungsi utama:**  
  - `clear_console()`  
    Membersihkan layar terminal secara lintas platform.  
    - Menggunakan perintah `cls` untuk Windows (`os.name == 'nt'`).  
    - Menggunakan perintah `clear` untuk Linux dan macOS.  
  - Mengembalikan kode status hasil eksekusi (`0` untuk sukses).  

---

### 🧩 Kesimpulan

Aplikasi **Flash Card App** dirancang dengan struktur modular untuk memisahkan tanggung jawab:
- `main.py` mengatur navigasi antarmuka utama.
- `app/exercises.py` fokus pada mode latihan tanpa penilaian.
- `app/quiz.py` menangani mode kuis dengan sistem penilaian dan penyimpanan hasil.
- `app/utils.py` mendukung operasi lintas platform seperti pembersihan layar.

Pendekatan ini memudahkan pengujian otomatis (`pytest`), pemeliharaan, serta pengembangan fitur lanjutan seperti mode belajar adaptif atau ekspor hasil ke format lain.

---

## 🧩 Tugas Anda

### 1️⃣ Lengkapi Kode yang Kosong
Setiap fungsi di bawah ini telah dikosongkan (hanya `pass` di dalamnya).  
Tugas Anda adalah **mengisi ulang** implementasi agar semua pengujian `pytest` lulus.

| File | Fungsi yang Harus Diimplementasikan |
|------|--------------------------------------|
| `app/utils.py` | `clear_console()` |
| `app/exercises.py` | `_load_flashcards()`, `run_exercises()` |
| `app/quiz.py` | `_load_flashcards()`, `_ensure_results_header()`, `_save_result()`, `_build_options()`, `_ask()`, `show_quiz()` |
| `main.py` | `main()` |
| _(Opsional)_ | Isi `STUDENT_ID` dan `STUDENT_NAME` di `main.py` |

> ⚠️ **PENTING:**  
> - Jangan ubah nama fungsi, argumen, konstanta, atau tipe nilai kembalian.
> - Hanya ubah kode yang ada di dalam fungsi serta `STUDENT_ID` dan `STUDENT_NAME` di `main.py`.  
> - Semua pengujian akan memeriksa nama dan perilaku fungsi secara otomatis.  
> - Fungsi harus mengikuti deskripsi (docstring) yang sudah tersedia.

---

### 2️⃣ Lengkapi Identitas Anda

Edit file `main.py` dan isi:
```python
STUDENT_ID = "2510101075"
STUDENT_NAME = "Nama Lengkap Anda"
```

**Syarat Validasi:**
- `STUDENT_ID` harus 10 digit numerik, contoh: `2510101075`.
- `STUDENT_NAME` minimal **3 karakter**, tanpa spasi di awal atau akhir.

---

## 🧪 Menjalankan Pengujian

Pastikan Anda berada di folder utama proyek (di mana `pytest.ini` berada).

### 1. Pastikan pip sudah terinstal

#### 🐧 Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3-pip -y
```

#### 🍎 macOS
```bash
brew install python3
# atau jika python3 sudah ada tapi pip belum:
python3 -m ensurepip --upgrade
```

#### 🪟 Windows
Buka Command Prompt (cmd) atau PowerShell, lalu jalankan:
```bash
python -m ensurepip --upgrade
```

---

### 2. Instal dependensi
```bash
pip install pytest
```

---

### 3. Jalankan semua pengujian
```bash
pytest -q
```

Jika semua implementasi benar, hasil akhirnya akan menampilkan:
```bash
....................  [100%]
28 passed in 0.05s
```
---

### 4. (Opsional) Jalankan dengan tampilan lebih detail
```bash
pytest -v
```

---

## 🧰 Referensi

- [Dokumentasi Python CSV](https://docs.python.org/3/library/csv.html)  
- [Dokumentasi pytest](https://docs.pytest.org/)  
- [Panduan Penulisan Kode Python (PEP8)](https://peps.python.org/pep-0008/)

---

## ✅ Checklist Sebelum Submit

- [ ] Semua fungsi telah diisi dan berjalan sesuai spesifikasi.  
- [ ] Semua tes `pytest` berhasil lulus tanpa error atau warning.  
- [ ] `STUDENT_ID` dan `STUDENT_NAME` telah diisi dengan benar.  
- [ ] Tidak ada perubahan pada nama fungsi, parameter, atau file.  

---

**Selamat mengerjakan dan semoga sukses menyelesaikan semua tes dengan pytest!**
