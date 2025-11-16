import tkinter as tk

class PackDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contoh pack() Lengkap")
        self.geometry("300x250")

        tk.Label(self, text="Atas", bg="lightblue").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Kiri", bg="yellow").pack(side="left", fill="y", padx=10, pady=10)
        tk.Button(self, text="Kanan", bg="cyan").pack(side="right", expand=True, padx=10, pady=10)
        tk.Label(self, text="Bawah", bg="lightgreen").pack(side="bottom", pady=5)

if __name__ == "__main__":
    app = PackDemo()
    app.mainloop()