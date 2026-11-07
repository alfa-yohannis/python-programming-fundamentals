import tkinter as tk
from second_form import SecondForm

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Form Utama")
        self.geometry("400x200")

        # Label sederhana
        self.label = tk.Label(self, text="Ini form utama.")
        self.label.pack(pady=20)

        # Menu bar
        menu_bar = tk.Menu(self)

        # Menu Navigasi
        menu_navigasi = tk.Menu(menu_bar, tearoff=0)
        menu_navigasi.add_command(label="Buka Form Kedua",
                                  command=self.buka_form_kedua)

        menu_bar.add_cascade(label="Navigasi", menu=menu_navigasi)

        # Tampilkan menu bar
        self.config(menu=menu_bar)

    def buka_form_kedua(self):
        # Membuka form kedua
        SecondForm(self)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()