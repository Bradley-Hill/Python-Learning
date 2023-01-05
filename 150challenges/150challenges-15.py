import tkinter as tk
from PIL import ImageTk, Image
import random

# # Challenge 133


# class MyGUI:
#     def __init__(self) -> None:
#         def hello_name():
#             name = text_box.get("1.0", "end")
#             output = str("Hello " + name)
#             output_box["text"] = output

#         self.root = tk.Tk()

#         self.root.title("My Second GUI")
#         self.root.iconbitmap("icon.ico")
#         self.root.geometry("800x600")

#         my_image = ImageTk.PhotoImage(Image.open("kabuki.jpg"))
#         my_image_label = tk.Label(self.root, image=my_image, justify="center")
#         my_image_label.grid(row=0, column=1)

#         label1 = tk.Label(self.root, text="Enter your name: ", font=("Arial", 16))
#         label1.grid(row=1, column=0)

#         text_box = tk.Text(self.root, height=1)
#         text_box.grid(row=1, column=1)

#         button = tk.Button(
#             self.root, text="Press me", font=("Helvetica", 14), command=hello_name
#         )
#         button.grid(row=2, column=0)

#         output_box = tk.Message(
#             self.root,
#         )
#         output_box.grid(row=2, column=1)

#         self.root.mainloop()


# MyGUI()

# Challenge 134


class MyGUI:
    def __init__(self) -> None:
        def check_answer():
            pass

        def next_question():
            pass

        self.root = tk.Tk()

        self.root.title("Maths questions")
        self.root.geometry("800x600")

        correct_image = ImageTk.PhotoImage(Image.open("#"))
        incorrect_image = ImageTk.PhotoImage(Image.open("#"))
        image_label = tk.Label(self.root, image="#", justify="center")


MyGUI()
