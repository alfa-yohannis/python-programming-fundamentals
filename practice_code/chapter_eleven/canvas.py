import tkinter as tk

class CanvasShapesDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Canvas: Gambar + Persegi + Segitiga")
        self.geometry("600x450")

        # Canvas
        self.canvas = tk.Canvas(self, width=560, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Load gambar PNG
        self.img = tk.PhotoImage(file="./image.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

        # Gambar bentuk
        self.gambar_bentuk()

    def gambar_bentuk(self):
        # Persegi
        self.canvas.create_rectangle(
            50, 50, 150, 150,
            outline="blue",
            width=3
        )

        # Segitiga
        self.canvas.create_polygon(
            250, 250,   # titik 1
            200, 350,   # titik 2
            300, 350,   # titik 3
            outline="red",
            fill="pink",
            width=2
        )

if __name__ == "__main__":
    app = CanvasShapesDemo()
    app.mainloop()
