import tkinter as tk

root = tk.Tk()
root.title("Contoh Label")

# Membuat label dengan teks sederhana
label1 = tk.Label(root, text="Halo, selamat datang di Tkinter!")

# Mengatur properti label: font, warna teks, dan latar
label2 = tk.Label(root,
                  text="Ini adalah label dengan properti.",
                  font=("Arial", 14),
                  fg="blue",
                  bg="lightgray")

# Menampilkan label pada window
label1.pack(pady=10)
label2.pack(pady=10)

root.mainloop()