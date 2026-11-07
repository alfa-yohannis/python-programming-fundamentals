import tkinter as tk
import time

class TriangleControlDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kontrol Segitiga Halus dengan Keyboard")
        self.geometry("400x400")

        # Canvas
        self.canvas = tk.Canvas(self, width=380, height=380, bg="white")
        self.canvas.pack(pady=10)

        # Buat segitiga
        self.triangle = self.canvas.create_polygon(
            190, 150,   # titik atas
            160, 200,   # titik kiri bawah
            220, 200,   # titik kanan bawah
            fill="blue"
        )

        # Kecepatan (px/s)
        self.vx = 0
        self.vy = 0
        self.speed = 160    # 160 px per detik

        # Delta time
        self.last = time.time()

        # Bind keyboard (tahan tombol → tetap bergerak)
        self.bind("<KeyPress>", self.on_key_down)
        self.bind("<KeyRelease>", self.on_key_up)
        self.focus_set()

        # Frame rate
        self.frame_delay = int(1000 / 60)  # 60 FPS

        # Mulai animasi
        self.update_anim()

    def on_key_down(self, event):
        if event.keysym == "Left":
            self.vx = -self.speed
        elif event.keysym == "Right":
            self.vx = self.speed
        elif event.keysym == "Up":
            self.vy = -self.speed
        elif event.keysym == "Down":
            self.vy = self.speed

    def on_key_up(self, event):
        # Saat tombol dilepas, hentikan gerakan pada arah itu
        if event.keysym in ("Left", "Right"):
            self.vx = 0
        if event.keysym in ("Up", "Down"):
            self.vy = 0

    def update_anim(self):
        now = time.time()
        dt = now - self.last
        self.last = now

        move_x = self.vx * dt
        move_y = self.vy * dt

        self.canvas.move(self.triangle, move_x, move_y)

        # Loop animasi 60 FPS
        self.after(self.frame_delay, self.update_anim)

if __name__ == "__main__":
    app = TriangleControlDemo()
    app.mainloop()
