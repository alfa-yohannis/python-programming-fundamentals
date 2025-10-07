"""
app/quiz.py — Modul Kuis Pilihan Ganda (Python 101)

Modul ini menjalankan kuis pilihan ganda berbasis flashcard yang dimuat dari berkas CSV.
Termasuk pemilihan soal acak, pengacakan opsi jawaban (1 benar + 2 pengecoh),
interaksi melalui konsol (print/input), serta pencatatan hasil kuis ke CSV.

Fitur Utama
-----------
1) Memuat flashcard (pertanyaan + jawaban) dari CSV: data/flashcards/python.csv
2) Menjalankan sesi kuis interaktif:
   - Memilih NUMBER_OF_QUESTIONS pertanyaan secara acak
   - Membangun opsi pilihan ganda dengan pengecoh dari jawaban lain
   - Menerima input pengguna (A/B/C atau 1/2/3), dukung keluar (Q/quit)
   - Menampilkan umpan balik benar/salah per soal
3) Menyimpan ringkasan hasil kuis ke CSV: data/results/results.csv
   - Kolom: timestamp, total_questions, correct, percentage

Dependensi
----------
- Standar Python: csv, os, random, datetime
- Utilitas lokal: app.utils.clear_console

Struktur Data & Asumsi CSV
--------------------------
- File sumber soal: data/flashcards/python.csv
- Format header: id, question, answer
- Setiap baris minimal memiliki kolom "question" dan "answer" yang tidak kosong
- Nilai dalam CSV boleh mengandung koma atau kutipan ganda; gunakan penulisan CSV yang benar
  (mis. kutip seluruh field atau escape sesuai standar CSV)

Konstanta
---------
- DATA_FILE: path sumber flashcard
- RESULTS_FILE: path hasil kuis
- NUMBER_OF_QUESTIONS: jumlah soal yang diambil per sesi (default: 5)

Ringkasan Fungsi
----------------
- _load_flashcards():
    Membaca seluruh flashcard dari CSV dan mengembalikan list[dict] dengan kunci "question" & "answer".
    Mengembalikan [] jika file tidak ditemukan, agar aplikasi tetap berjalan.

- _build_options(correct_answer, all_answers, k=3):
    Menyusun k opsi jawaban (1 benar + k-1 pengecoh) lalu mengacak urutannya.
    Jika pool pengecoh kecil, fungsi melakukan padding (duplikasi) agar jumlah tetap k.

- _ask(q_number, total, question, options, correct_answer):
    Menampilkan satu pertanyaan + opsi (A/B/C), menerima input, menilai jawaban,
    memberi umpan balik, dan mengembalikan True/False/None (keluar).

- _ensure_results_header():
    Memastikan direktori & file hasil tersedia. Jika kosong/belum ada, tulis header standar.

- _save_result(total, correct):
    Menghitung persentase dan menambahkan baris hasil ke RESULTS_FILE (timestamp ISO, total, benar, %).

- show_quiz():
    Titik masuk mode kuis interaktif: memuat soal, memilih acak, bertanya satu per satu,
    menampilkan ringkasan, dan menyimpan hasil.

Alur Eksekusi (Ringkas)
-----------------------
main() ─▶ show_quiz()
          ├─▶ _load_flashcards()
          ├─▶ (loop pertanyaan)
          │     ├─▶ _build_options()
          │     └─▶ _ask()
          └─▶ _save_result() ─▶ _ensure_results_header()

Perilaku & I/O
--------------
- Aplikasi berinteraksi melalui terminal:
  - Input: A/B/C atau 1/2/3 (jawab), Q/quit (keluar)
  - Output: pertanyaan, opsi, umpan balik, ringkasan
- clear_console() dipanggil untuk merapikan tampilan antar langkah

Catatan Pengujian
-----------------
- Saat pengujian otomatis (pytest), gunakan monkeypatch:
  - Monkeypatch input() untuk menyimulasikan jawaban
  - Monkeypatch clear_console() agar tidak benar-benar membersihkan layar
  - Arahkan DATA_FILE & RESULTS_FILE ke direktori sementara (tmp_path)

Lisensi & Tujuan
----------------
- Ditujukan untuk latihan/edukasi pemrograman dasar Python (Python 101).
- Kode ini sederhana dan dapat disesuaikan untuk kebutuhan pembelajaran lanjutan.
"""

# app/quiz.py
import csv
import os
import random
from datetime import datetime
from app.utils import clear_console

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "flashcards", "python.csv")
RESULTS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "results", "results.csv")
NUMBER_OF_QUESTIONS = 5  # pick this many random questions per test


def _load_flashcards():
    """
    Memuat (membaca) data flashcard dari file CSV ke dalam bentuk daftar (list) berisi dictionary.

    Fungsi ini digunakan untuk mengambil seluruh data pertanyaan dan jawaban
    yang tersimpan dalam file CSV agar dapat digunakan pada sesi kuis atau latihan interaktif.
    File yang digunakan terletak di:
        data/flashcards/python.csv

    Format file yang diharapkan:
        Header: id, question, answer
        Contoh isi:
            1,"Apa itu Python?","Bahasa pemrograman"
            2,"Simbol penugasan di Python?","="

    Tujuan:
        Mengonversi data dalam file CSV menjadi struktur data Python yang mudah diolah
        oleh fungsi lain seperti `show_quiz()` atau `show_tests()`.

    Proses:
        1. Membuka file CSV yang ditentukan oleh variabel global `DATA_FILE`.
        2. Membaca setiap baris menggunakan `csv.DictReader`.
        3. Mengambil nilai dari kolom `question` dan `answer` lalu membersihkan spasi berlebih.
        4. Menyimpan setiap entri valid ke dalam list dalam bentuk:
              {"question": "...", "answer": "..."}
        5. Jika file tidak ditemukan (`FileNotFoundError`), fungsi tidak akan menghasilkan error
           melainkan hanya mengembalikan list kosong agar aplikasi tetap berjalan.

    Parameter:
        (tidak memiliki parameter)

    Nilai Kembalian:
        list[dict]:
            Daftar flashcard yang berisi pasangan pertanyaan dan jawaban.
            Contoh hasil:
                [
                    {"question": "Apa itu Python?", "answer": "Bahasa pemrograman"},
                    {"question": "Simbol penugasan di Python?", "answer": "="}
                ]

    Kapan dan di mana fungsi ini dipanggil:
        Fungsi ini dipanggil **di awal proses kuis**, tepatnya di dalam `show_quiz()` (atau `show_tests()`
        pada modul lain yang sejenis), untuk mengambil seluruh flashcard dari file CSV
        sebelum memilih pertanyaan secara acak untuk ditampilkan ke pengguna.

    Alur Pemanggilan Fungsi:
        show_quiz() ─▶ _load_flashcards()

    Contoh Penggunaan:
        >>> cards = _load_flashcards()
        >>> print(len(cards))
        10
        >>> print(cards[0])
        {'question': 'Apa itu Python?', 'answer': 'Bahasa pemrograman'}
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


def _ensure_results_header():
    """
    Memastikan file hasil kuis ('data/results/results.csv') tersedia dan memiliki header yang benar.

    Fungsi ini bertugas untuk:
    1. Membuat direktori `data/results/` jika belum ada.
    2. Membuat file `results.csv` dengan header kolom:
         ["timestamp", "total_questions", "correct", "percentage"]
       apabila file tersebut belum ada atau masih kosong.

    Tujuan utama:
        Menjaga agar file hasil kuis memiliki struktur yang konsisten sebelum
        proses penyimpanan hasil dilakukan oleh fungsi `_save_result()`.

    Parameter:
        (tidak memiliki parameter)

    Nilai Kembalian:
        Tidak mengembalikan nilai (None). Fungsi ini hanya memastikan file tersedia.

    Proses:
        - Mengecek apakah folder hasil (`data/results/`) sudah ada; jika belum, akan dibuat.
        - Mengecek apakah file hasil (`results.csv`) ada dan memiliki isi.
          Jika belum ada atau kosong, maka file baru akan dibuat dengan header standar.

    Kapan dan di mana fungsi ini dipanggil:
        Fungsi ini dipanggil **secara otomatis di awal fungsi `_save_result()`**, sebelum data hasil kuis disimpan.
        Dengan demikian, `_ensure_results_header()` menjamin struktur file hasil selalu valid dan siap digunakan
        meskipun ini adalah pencatatan hasil pertama kali.

    Alur Pemanggilan Fungsi:
        show_tests() ─▶ _save_result() ─▶ _ensure_results_header()

    Contoh hasil file setelah pemanggilan pertama:
        timestamp,total_questions,correct,percentage
    """
    os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
    if not os.path.exists(RESULTS_FILE) or os.path.getsize(RESULTS_FILE) == 0:
        with open(RESULTS_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "total_questions", "correct", "percentage"])


def _save_result(total, correct):
    """
    Menyimpan hasil tes ke dalam berkas CSV.

    Fungsi ini digunakan untuk mencatat ringkasan hasil ujian (jumlah soal,
    jawaban benar, dan persentase skor) ke dalam file hasil (`results.csv`).
    Jika file belum ada, fungsi `_ensure_results_header()` akan memastikan
    header kolom dibuat terlebih dahulu.

    Argumen:
        total (int): Jumlah total pertanyaan yang dijawab.
        correct (int): Jumlah jawaban yang benar.

    Proses:
        1. Memanggil `_ensure_results_header()` untuk memastikan file hasil sudah siap.
        2. Menghitung persentase skor (`percentage`) dengan dua angka di belakang koma.
        3. Menambahkan baris baru ke file CSV berisi:
           - timestamp waktu saat tes disimpan (format ISO),
           - total pertanyaan,
           - jumlah benar,
           - dan persentase skor.

    Contoh format hasil di file `results.csv`:
        timestamp,total_questions,correct,percentage
        2025-10-07T12:45:33,5,4,80.0

    Kapan dan di mana fungsi ini dipanggil:
        Fungsi ini dipanggil **di akhir proses tes**, tepatnya di fungsi `show_tests()`,
        setelah semua pertanyaan selesai dijawab atau peserta keluar dari tes.
        Tujuannya adalah menyimpan ringkasan hasil ke folder:
            data/results/results.csv
        sehingga dapat digunakan untuk pelaporan atau analisis hasil latihan.
    """
    _ensure_results_header()
    pct = round((correct / total) * 100, 2) if total else 0.0
    with open(RESULTS_FILE, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow([datetime.now().isoformat(timespec="seconds"), total, correct, pct])


def _build_options(correct_answer, all_answers, k=3):
    """
    Membentuk daftar opsi jawaban (multiple choice) berisi satu jawaban benar
    dan beberapa opsi pengecoh (distractors), kemudian mengacak urutannya.

    Tujuan:
        Fungsi ini digunakan untuk membangun daftar pilihan jawaban pada
        sesi kuis atau tes interaktif. Setiap pertanyaan akan menampilkan
        satu jawaban benar dan beberapa opsi salah yang diambil dari daftar
        jawaban lain.

    Parameter:
        correct_answer (str): Jawaban yang benar untuk pertanyaan saat ini.
        all_answers (list[str]): Daftar semua jawaban yang tersedia dari seluruh flashcard.
        k (int): Jumlah total opsi yang ingin ditampilkan (default = 3).
                 Termasuk 1 jawaban benar + (k-1) opsi pengecoh.

    Proses:
        1. Menentukan jumlah pengecoh yang diperlukan (`need = k - 1`).
        2. Membuat kumpulan jawaban unik selain jawaban benar.
        3. Mengacak kumpulan unik tersebut dan mengambil sejumlah opsi pengecoh.
        4. Jika jumlah pengecoh belum cukup:
            - Mengambil tambahan dari kumpulan semua jawaban (`pool_all`) tanpa duplikasi.
        5. Jika data masih kurang (misalnya hanya satu jawaban di dataset),
            maka fungsi akan mengisi sisanya dengan pengulangan (padding)
            agar jumlah total tetap sama dengan `k`.
        6. Menyusun daftar akhir dengan menambahkan jawaban benar,
           lalu mengacak urutannya agar posisi jawaban benar tidak selalu sama.
        7. Mengembalikan `k` opsi jawaban akhir dalam urutan acak.

    Nilai Kembalian:
        list[str]: Daftar berisi `k` opsi jawaban acak.
                   Contoh: ["def", "for", "if"]

    Penanganan Khusus:
        - Jika `k <= 0`, fungsi akan langsung mengembalikan list kosong `[]`.
        - Jika jumlah jawaban unik terlalu sedikit, fungsi akan mengulang opsi yang ada
          agar tetap memenuhi jumlah total `k`.

    Kapan dan di mana fungsi ini dipanggil:
        Fungsi ini dipanggil oleh `show_tests()` (atau `show_quiz()`) untuk setiap
        pertanyaan yang akan ditampilkan kepada pengguna.  
        Tepatnya, pemanggilan terjadi sebelum fungsi `_ask()` dijalankan,
        untuk menyiapkan tiga opsi pilihan ganda yang akan ditampilkan di layar.

    Alur Pemanggilan Fungsi:
        show_tests() ─▶ _build_options() ─▶ _ask()

    Contoh Penggunaan:
        >>> answers = ["def", "for", "if", "while", "return"]
        >>> opts = _build_options("def", answers, k=3)
        >>> print(opts)
        ['if', 'def', 'for']  # urutan acak

    Contoh Kasus Khusus (pool kecil):
        >>> _build_options("A", ["A"], k=3)
        ['A', 'A', 'A']  # duplikasi otomatis untuk menjaga jumlah tetap 3
    """
    import random

    if k <= 0:
        return []

    need = k - 1  # jumlah pengecoh yang diperlukan

    # Kumpulan jawaban unik selain jawaban benar
    pool_unique = [a for a in set(all_answers) if a != correct_answer]
    random.shuffle(pool_unique)

    distractors = pool_unique[:need]

    # Jika masih kurang, gunakan kumpulan non-unik
    if len(distractors) < need:
        pool_all = [a for a in all_answers if a != correct_answer]
        random.shuffle(pool_all)
        for a in pool_all:
            if len(distractors) >= need:
                break
            if a not in distractors:
                distractors.append(a)

        # Jika tetap kurang, isi dengan pengulangan (padding)
        while len(distractors) < need:
            filler = distractors[0] if distractors else correct_answer
            distractors.append(filler)

    options = [correct_answer] + distractors[:need]
    random.shuffle(options)
    return options[:k]




def _ask(q_number, total, question, options, correct_answer):
    """
    Menampilkan satu pertanyaan kuis ke layar dan meminta jawaban dari pengguna.

    Fungsi ini merupakan inti dari interaksi pengguna dalam sesi kuis.
    Ia menampilkan teks pertanyaan, daftar opsi jawaban (A/B/C),
    menerima input pengguna, memberikan umpan balik (benar/salah),
    dan mengembalikan hasil jawaban dalam bentuk nilai boolean.

    Tujuan:
        Untuk menampilkan pertanyaan dan menilai apakah jawaban pengguna benar,
        salah, atau jika pengguna memilih untuk keluar dari kuis.

    Parameter:
        q_number (int):
            Nomor pertanyaan saat ini (misal 1 untuk pertanyaan pertama).
        total (int):
            Total jumlah pertanyaan dalam sesi kuis.
        question (str):
            Teks pertanyaan yang akan ditampilkan ke layar.
        options (list[str]):
            Daftar opsi jawaban, biasanya 3 elemen hasil dari `_build_options()`.
            Contoh: ["def", "for", "if"]
        correct_answer (str):
            Jawaban yang benar untuk pertanyaan tersebut.

    Proses:
        1. Membersihkan layar konsol menggunakan `clear_console()`.
        2. Menampilkan judul dan nomor pertanyaan (misalnya: “Python Test — Question 1/5”).
        3. Menampilkan teks pertanyaan dan tiga opsi jawaban (A, B, C).
        4. Menunggu input dari pengguna:
             - “A”, “B”, “C” atau “1”, “2”, “3” untuk memilih jawaban.
             - “Q” atau “quit” untuk keluar dari sesi kuis lebih awal.
        5. Mengevaluasi apakah jawaban pengguna benar (`True`), salah (`False`), atau keluar (`None`).
        6. Menampilkan umpan balik di layar:
             - “Correct!” jika benar.
             - “Incorrect. Correct answer: ...” jika salah.
        7. Menunggu pengguna menekan Enter sebelum melanjutkan ke pertanyaan berikutnya.

    Nilai Kembalian:
        bool | None:
            - `True`  → jika pengguna menjawab dengan benar.
            - `False` → jika pengguna menjawab salah.
            - `None`  → jika pengguna memilih keluar dengan menekan “Q” atau “quit”.

    Kapan dan di mana fungsi ini dipanggil:
        Fungsi ini dipanggil **di dalam `show_tests()`** (atau `show_quiz()`),
        setelah opsi jawaban dibentuk oleh `_build_options()`.
        Pemanggilan terjadi berulang kali, sekali untuk setiap pertanyaan yang ditampilkan
        selama sesi kuis berlangsung.

    Alur Pemanggilan Fungsi:
        show_tests() ─▶ _build_options() ─▶ _ask()

    Contoh Penggunaan:
        >>> q = "Simbol untuk mendefinisikan fungsi di Python?"
        >>> opts = ["def", "for", "if"]
        >>> _ask(1, 5, q, opts, "def")
        (Menunggu input pengguna di terminal)
        # Output:
        # Python Test — Question 1/5
        # Q: Simbol untuk mendefinisikan fungsi di Python?
        # A. def
        # B. for
        # C. if
        # (Type A/B/C or 1/2/3. Q to quit test.)
        # Your answer: a
        # Correct!

    Catatan:
        - Fungsi ini bersifat **interaktif** dan hanya bekerja pada terminal (console).
        - Jika digunakan dalam pengujian otomatis, input perlu disimulasikan
          menggunakan `monkeypatch` atau fungsi mock input.

    """
    clear_console()
    print(f"Python Test — Question {q_number}/{total}\n")
    print("Q:", question, "\n")

    labels = ["A", "B", "C"]
    for i, opt in enumerate(options):
        print(f"{labels[i]}. {opt}")

    print("\n(Type A/B/C or 1/2/3. Q to quit test.)")

    while True:
        choice = input("Your answer: ").strip().lower()
        if choice in ("a", "b", "c"):
            idx = {"a": 0, "b": 1, "c": 2}[choice]
            break
        elif choice in ("1", "2", "3"):
            idx = int(choice) - 1
            break
        elif choice in ("q", "quit"):
            return None
        else:
            print("Invalid input. Please type A/B/C, 1/2/3, or Q.")
            input("\nPress Enter to continue...")

    is_correct = options[idx] == correct_answer
    print("\nCorrect!" if is_correct else f"\nIncorrect. Correct answer: {correct_answer}")
    input("\nPress Enter for next...")
    return is_correct



def show_quiz():
    """
    Memulai sesi kuis secara langsung (tanpa menu):
    memilih NUMBER_OF_QUESTIONS pertanyaan acak dan menjalankan kuis pilihan ganda.

    Tujuan:
        Menjalankan seluruh alur kuis dari awal hingga ringkasan hasil:
        - Memuat flashcards dari CSV
        - Memilih sejumlah pertanyaan secara acak
        - Menyusun opsi jawaban (1 benar + 2 pengecoh)
        - Menanyakan setiap pertanyaan ke pengguna
        - Menampilkan ringkasan skor
        - Menyimpan hasil ke file CSV

    Proses:
        1) Memanggil `_load_flashcards()` untuk membaca semua kartu soal.
           - Jika kosong/tidak ditemukan, tampilkan informasi path yang diharapkan dan kembali.
        2) Menentukan jumlah pertanyaan yang akan ditanyakan:
           `min(NUMBER_OF_QUESTIONS, len(cards))`.
        3) Mengambil sampel pertanyaan acak dengan `random.sample`.
        4) Untuk setiap pertanyaan terpilih:
           - Bangun opsi jawaban via `_build_options()` (3 opsi).
           - Tampilkan pertanyaan dan minta jawaban via `_ask()`.
           - Tangani hasil: `True` (benar), `False` (salah), atau `None` (keluar).
        5) Setelah loop:
           - Jika tidak ada pertanyaan yang dijawab (user keluar di awal), cetak "Test canceled." dan kembali.
           - Jika ada, hitung persentase skor, tampilkan ringkasan, lalu simpan ringkasan dengan `_save_result()`.

    Parameter:
        (tidak ada)

    Nilai Kembalian:
        None — Fungsi ini bersifat prosedural dan berinteraksi langsung dengan terminal.

    Kapan dan di mana fungsi ini dipanggil:
        - Dipanggil dari lapisan antarmuka utama (mis. `main.py`) saat pengguna memilih mode Kuis/Test.
        - Fungsi ini adalah titik masuk utama untuk mode kuis interaktif.

    Ketergantungan internal:
        - `_load_flashcards()`   : Memuat data soal-jawaban dari CSV.
        - `_build_options()`     : Menyusun opsi jawaban (multiple choice).
        - `_ask()`               : Menampilkan 1 soal dan memproses jawaban pengguna.
        - `_save_result()`       : Menyimpan ringkasan hasil kuis ke CSV.
        - `_ensure_results_header()` (dipanggil di dalam `_save_result()`).

    Alur Pemanggilan Fungsi:
        main() ─▶ show_quiz()
                    ├─▶ _load_flashcards()
                    ├─▶ _build_options()
                    ├─▶ _ask()
                    └─▶ _save_result() ─▶ _ensure_results_header()

    Catatan:
        - Fungsi ini bergantung pada I/O terminal (print/input) sehingga pada pengujian otomatis
          biasanya input disimulasikan (monkeypatch).
        - Jika dataset kecil, `_build_options()` dapat melakukan padding (duplikasi) agar jumlah opsi tetap 3.
    """

    cards = _load_flashcards()
    if not cards:
        clear_console()
        print("No flashcards found.")
        print(f"Expected file: {os.path.abspath(DATA_FILE)}")
        input("\nPress Enter to go back...")
        return

    total_questions = min(NUMBER_OF_QUESTIONS, len(cards))
    selected = random.sample(cards, total_questions)
    all_answers = [c["answer"] for c in cards]

    correct_count = 0
    asked = 0

    for i, card in enumerate(selected, 1):
        q = card["question"]
        correct = card["answer"]
        options = _build_options(correct, all_answers, k=3)

        result = _ask(i, total_questions, q, options, correct)
        if result is None:
            break  # pengguna memilih keluar
        asked += 1
        if result:
            correct_count += 1

    clear_console()
    if asked == 0:
        print("Test canceled.")
        return

    pct = round((correct_count / asked) * 100, 2)
    print("Test Summary")
    print(f"Questions answered : {asked}")
    print(f"Correct answers    : {correct_count}")
    print(f"Score              : {pct}%")

    _save_result(asked, correct_count)
    input("\nPress Enter to return...")

