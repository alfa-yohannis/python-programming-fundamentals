import tkinter as tk

class MenuDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Judul Awal")
        self.geometry("300x150")

        # Membuat menu bar
        menu_bar = tk.Menu(self)

        # Membuat menu "File"
        menu_file = tk.Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Ubah Judul", command=self.ubah_judul)

        # Menambahkan menu ke menu bar
        menu_bar.add_cascade(label="File", menu=menu_file)

        # Menampilkan menu bar
        self.config(menu=menu_bar)

    # Method yang dipanggil dari menu
    def ubah_judul(self):
        self.title("Judul Berubah!")

if __name__ == "__main__":
    app = MenuDemo()
    app.mainloop()