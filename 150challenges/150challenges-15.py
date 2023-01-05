import tkinter as tk
from PIL import ImageTk, Image

# Challenge 133


class MyGUI:
    def __init__(self) -> None:

        self.root = tk.Tk()

        self.root.title("My Second GUI")
        self.root.iconbitmap("icon.ico")
        self.root.geometry("800x600")

        my_image = ImageTk.PhotoImage(Image.open("logo.gif"))
        my_label = tk.Label(self.root, image=my_image, justify="center")
        my_label.pack(padx=10, pady=10)

        self.root.mainloop()


MyGUI()
