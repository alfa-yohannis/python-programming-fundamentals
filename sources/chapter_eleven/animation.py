import tkinter as tk
import time

class AnimasiCanvas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Animasi Halus di Canvas")
        self.geometry("400x300")

        self.canvas = tk.Canvas(self, width=380, height=250, bg="white")
        self.canvas.pack(pady=10)

        # Buat bola
        self.x_pos = 10
        self.y_pos = 100
        self.ball = self.canvas.create_oval(
            self.x_pos, self.y_pos,
            self.x_pos + 30, self.y_pos + 30,
            fill="blue"
        )

        # Kecepatan dalam pixel/s
        self.dx = 120        # 120 px per detik

        # Untuk delta time
        self.last = time.time()

        # Target frame rate
        self.frame_delay = int(1000 / 60)   # 60 FPS → ~16 ms

        self.gerak()

    def gerak(self):
        now = time.time()
        dt = now - self.last
        self.last = now

        # Hitung jarak berdasarkan dt
        move_x = self.dx * dt
        self.x_pos += move_x

        # Bouncing
        if self.x_pos >= 350:
            self.dx = -abs(self.dx)
        if self.x_pos <= 0:
            self.dx = abs(self.dx)

        # Gerakkan bola
        self.canvas.move(self.ball, move_x, 0)

        # Jadwalkan frame berikutnya (60 FPS)
        self.after(self.frame_delay, self.gerak)


if __name__ == "__main__":
    app = AnimasiCanvas()
    app.mainloop()
