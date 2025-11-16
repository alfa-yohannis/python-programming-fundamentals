import tkinter as tk

class SecondForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Form Kedua")
        self.geometry("300x150")
        # Tidak ada komponen tambahan (form kosong)