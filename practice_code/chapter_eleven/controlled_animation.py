import tkinter as tk

class TriangleControlDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kontrol Segitiga dengan Keyboard")
        self.geometry("400x400")

        # Canvas
        self.canvas = tk.Canvas(self, width=380, height=380, bg="white")
        self.canvas.pack(pady=10)

        # Buat segitiga (x1, y1, x2, y2, x3, y3)
        self.triangle = self.canvas.create_polygon(
            190, 150,   # titik atas
            160, 200,   # titik kiri bawah
            220, 200,   # titik kanan bawah
            fill="blue"
        )

        # Jarak gerak setiap kali tombol ditekan
        self.step = 10

        # Bind keyboard ke window
        self.bind("<KeyPress>", self.on_key)
        # Pastikan window punya fokus keyboard
        self.focus_set()

    def on_key(self, event):
        # Cek tombol apa yang ditekan
        if event.keysym == "Left":
            self.canvas.move(self.triangle, -self.step, 0)
        elif event.keysym == "Right":
            self.canvas.move(self.triangle, self.step, 0)
        elif event.keysym == "Up":
            self.canvas.move(self.triangle, 0, -self.step)
        elif event.keysym == "Down":
            self.canvas.move(self.triangle, 0, self.step)

if __name__ == "__main__":
    app = TriangleControlDemo()
    app.mainloop()
