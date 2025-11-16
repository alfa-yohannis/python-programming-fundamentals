import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class GambarDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contoh Menampilkan Gambar")
        self.geometry("400x300")

        self.label_gambar = tk.Label(self)
        self.label_gambar.pack(pady=10)

        self.button = tk.Button(self, text="Pilih Gambar", command=self.pilih_gambar)
        self.button.pack(pady=10)

    def pilih_gambar(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
        )

        if filepath:
            img = Image.open(filepath)
            img = img.resize((300, 200))  # optional, supaya muat
            tk_img = ImageTk.PhotoImage(img)
            self.label_gambar.img = tk_img   # simpan referensi
            self.label_gambar.config(image=tk_img)

if __name__ == "__main__":
    app = GambarDemo()
    app.mainloop()
