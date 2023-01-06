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

        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
        num3 = str(num1)
        num4 = str(num2)
        question = num3, "+", num4

        def check_answer():
            answer = int(entry_box.get())
            act_answer = num1 + num2
            if answer == act_answer:
                image_label.config(image=correct_image)
            else:
                image_label.config(image=incorrect_image)

        def next_question():
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
            num3 = str(num1)
            num4 = str(num2)
            question = num3, "+", num4
            question_label.config(text=question)
            image_label.config(image="")

        self.root = tk.Tk()

        self.root.title("Maths questions")
        self.root.geometry("800x900")

        correct_image = ImageTk.PhotoImage(Image.open("correct.jpg"))
        incorrect_image = ImageTk.PhotoImage(Image.open("incorrect.jpg"))
        image_label = tk.Label(self.root, justify="center")
        image_label.pack()

        question_label = tk.Label(self.root, text=question, font=("Arial", 16))
        question_label.pack(padx=5, pady=5)

        entry_label = tk.Label(
            font=("Arial", 16), text="Please enter the correct answer."
        )
        entry_label.pack(padx=5, pady=5)

        entry_box = tk.Entry(
            self.root, textvariable="Enter the correct answer", font=("Arial", 18)
        )
        entry_box.pack()

        button_check = tk.Button(
            text="Check Answer", command=check_answer, font=("Arial", 14)
        )
        button_check.pack()

        button_next = tk.Button(
            text="Next question", command=next_question, font=("Arial", 14)
        )
        button_next.pack()

        self.root.mainloop()


MyGUI()
