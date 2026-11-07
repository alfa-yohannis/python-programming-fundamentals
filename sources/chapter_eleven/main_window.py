import tkinter as tk

# Membuat kelas untuk window utama
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Mengatur judul jendela
        self.title("Aplikasi Tkinter Pertama")

        # Mengatur ukuran jendela
        self.geometry("400x300")

# Menjalankan aplikasi
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()