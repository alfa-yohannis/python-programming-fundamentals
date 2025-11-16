import tkinter as tk

class AnimasiCanvas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Animasi di Canvas")
        self.geometry("400x300")

        # Canvas tempat animasi
        self.canvas = tk.Canvas(self, width=380, height=250, bg="white")
        self.canvas.pack(pady=10)

        # Membuat lingkaran (bola)
        self.x_pos = 10
        self.y_pos = 100
        self.ball = self.canvas.create_oval(self.x_pos, self.y_pos,
                                            self.x_pos + 30, self.y_pos + 30,
                                            fill="blue")

        # Kecepatan gerak
        self.x_speed = 1

        # Mulai animasi
        self.gerak()

    def gerak(self):
        # Update posisi bola
        self.x_pos += self.x_speed

        # Jika bola menyentuh batas kanan → balik arah
        if self.x_pos >= 350:
            self.x_speed = -1

        # Jika bola menyentuh batas kiri → balik arah
        if self.x_pos <= 0:
            self.x_speed = 1

        # Geser objek pada canvas
        self.canvas.coords(self.ball,
                           self.x_pos, self.y_pos,
                           self.x_pos + 30, self.y_pos + 30)

        # Panggil ulang fungsi ini setiap 20 ms (50 FPS)
        self.after(20, self.gerak)

if __name__ == "__main__":
    app = AnimasiCanvas()
    app.mainloop()
