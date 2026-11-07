import tkinter as tk
from tkinter import ttk

class TableDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contoh Tabel Data")
        self.geometry("400x250")

        # Frame untuk menampung tabel dan scrollbar
        frame_table = tk.Frame(self)
        frame_table.pack(fill="both", expand=True, pady=10, padx=10)

        # Membuat Treeview dengan dua kolom
        self.tree = ttk.Treeview(
            frame_table,
            columns=("nama", "umur"),
            show="headings"  # hanya menampilkan header, tanpa kolom tree
        )

        # Mengatur header kolom
        self.tree.heading("nama", text="Nama")
        self.tree.heading("umur", text="Umur")

        # Mengatur lebar kolom
        self.tree.column("nama", width=200)
        self.tree.column("umur", width=80, anchor="center")

        # Menambahkan beberapa baris data
        self.tree.insert("", tk.END, values=("Andi", 20))
        self.tree.insert("", tk.END, values=("Budi", 21))
        self.tree.insert("", tk.END, values=("Citra", 19))

        # Scrollbar vertikal
        scrollbar = tk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Menempatkan tabel dan scrollbar berdampingan
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Label untuk menampilkan baris terpilih
        self.label_info = tk.Label(self, text="Belum ada baris yang dipilih")
        self.label_info.pack(pady=5)

        # Tombol untuk mengambil data baris terpilih
        button_pilih = tk.Button(self, text="Tampilkan Baris Terpilih",
                                 command=self.tampilkan_pilihan)
        button_pilih.pack(pady=5)

    def tampilkan_pilihan(self):
        # Mengambil item yang sedang dipilih
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            self.label_info.config(text=f"Terpilih: Nama = {values[0]}, Umur = {values[1]}")
        else:
            self.label_info.config(text="Belum ada baris yang dipilih")

if __name__ == "__main__":
    app = TableDemo()
    app.mainloop()