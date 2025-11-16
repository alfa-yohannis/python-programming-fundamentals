import tkinter as tk

class ButtonDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contoh Button")
        self.geometry("300x200")

        # Label awal
        self.label = tk.Label(self, text="Teks awal")
        self.label.pack(pady=10)

        # Button yang memanggil method saat ditekan
        self.button = tk.Button(self, text="Klik Saya", command=self.ubah_teks)
        self.button.pack(pady=10)

    # Event handler dalam bentuk method
    def ubah_teks(self):
        self.label.config(text="Tombol ditekan!")

if __name__ == "__main__":
    app = ButtonDemo()
    app.mainloop()