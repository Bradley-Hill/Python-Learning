import tkinter as tk
from tkinter import StringVar
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

# # Challenge 134


# class MyGUI:
#     def __init__(self) -> None:

#         num1 = random.randint(10, 50)
#         num2 = random.randint(10, 50)
#         num3 = str(num1)
#         num4 = str(num2)
#         question = num3, "+", num4

#         def check_answer():
#             answer = int(entry_box.get())
#             act_answer = num1 + num2
#             if answer == act_answer:
#                 image_label.config(image=correct_image)
#             else:
#                 image_label.config(image=incorrect_image)

#         def next_question():
#             num1 = random.randint(10, 50)
#             num2 = random.randint(10, 50)
#             num3 = str(num1)
#             num4 = str(num2)
#             question = num3, "+", num4
#             question_label.config(text=question)
#             image_label.config(image="")

#         self.root = tk.Tk()

#         self.root.title("Maths questions")
#         self.root.geometry("800x900")

#         correct_image = ImageTk.PhotoImage(Image.open("correct.jpg"))
#         incorrect_image = ImageTk.PhotoImage(Image.open("incorrect.jpg"))
#         image_label = tk.Label(self.root, justify="center")
#         image_label.pack()

#         question_label = tk.Label(self.root, text=question, font=("Arial", 16))
#         question_label.pack(padx=5, pady=5)

#         entry_label = tk.Label(
#             font=("Arial", 16), text="Please enter the correct answer."
#         )
#         entry_label.pack(padx=5, pady=5)

#         entry_box = tk.Entry(
#             self.root, textvariable="Enter the correct answer", font=("Arial", 18)
#         )
#         entry_box.pack()

#         button_check = tk.Button(
#             text="Check Answer", command=check_answer, font=("Arial", 14)
#         )
#         button_check.pack()

#         button_next = tk.Button(
#             text="Next question", command=next_question, font=("Arial", 14)
#         )
#         button_next.pack()

#         self.root.mainloop()


# MyGUI()

# # Challenge 135


# class MyGUI:
#     def __init__(self) -> None:
#         def change_background():
#             self.root.configure(background=clicked.get())
#             pass

#         self.root = tk.Tk()

#         self.root.title("Background Colour Selector")
#         self.root.geometry("400x400")

#         colours = ["", "red", "green", "blue", "grey", "yellow"]

#         clicked = StringVar(self.root)
#         clicked.set(colours[0])

#         list_menu = tk.OptionMenu(self.root, clicked, *colours)
#         list_menu.pack()

#         click_me = tk.Button(
#             self.root,
#             text="Change Background",
#             command=change_background,
#             font=("Arial", 18),
#         )
#         click_me.pack()

#         self.root.mainloop()


# MyGUI()

# # Challenge 136


# class MyGUI:
#     def __init__(self) -> None:
#         def add_to_list():
#             gender_choice = clicked.get()
#             name_choice = name.get()
#             list_entry = name_choice, ",", gender_choice
#             list_box.insert("end", list_entry)
#             pass

#         self.root = tk.Tk()

#         self.root.title("Name and Gender")
#         self.root.geometry("400x400")

#         gender = ["", "Female", "Male"]

#         clicked = StringVar(self.root)
#         clicked.set(gender[0])

#         name = tk.Entry(
#             self.root,
#         )
#         name.pack()

#         list_menu = tk.OptionMenu(self.root, clicked, *gender)
#         list_menu.pack()

#         list_box = tk.Listbox(self.root)
#         list_box.pack()

#         click_me = tk.Button(
#             self.root,
#             text="Add to list",
#             command=add_to_list,
#             font=("Arial", 18),
#         )
#         click_me.pack()

#         self.root.mainloop()


# MyGUI()

# # Challenge 137
# class MyGUI:
#     def __init__(self) -> None:
#         def add_to_list():
#             gender_choice = str(clicked.get())
#             name_choice = str(name.get())
#             list_entry = name_choice + "," + gender_choice + "\n"
#             list_box.insert("end", list_entry)
#             text_file = open("namelist.txt", "a+")
#             list_entry = str(list_entry)
#             text_file.write(list_entry)
#             text_file.close

#         def display_text():
#             file = open("namelist.txt", "r")
#             display_text = file.read()
#             text_box.insert("1.0", display_text)
#             file.close()

#         self.root = tk.Tk()

#         self.root.title("Name and Gender")
#         self.root.geometry("400x400")

#         gender = ["", "Female", "Male"]

#         clicked = StringVar(self.root)
#         clicked.set(gender[0])

#         name = tk.Entry(
#             self.root,
#         )
#         name.pack()

#         list_menu = tk.OptionMenu(self.root, clicked, *gender)
#         list_menu.pack()

#         list_box = tk.Listbox(self.root)
#         list_box.pack()

#         text_box = tk.Text(self.root, font=("Helvetica", 16))
#         text_box.pack()

#         click_me = tk.Button(
#             self.root,
#             text="Add to list",
#             command=add_to_list,
#             font=("Arial", 18),
#         )
#         click_me.pack()

#         display_txt_file = tk.Button(
#             self.root, text="Display text File", command=display_text
#         )
#         display_txt_file.pack()

#         self.root.mainloop()


# MyGUI()

# Challenge 138


class MyGUI:
    def __init__(self) -> None:
        def image_selector():
            image_selection = choice.get()
            image_selection = int(image_selection)
            if image_selection == 1:
                picture_label.config(image=my_image1)
            elif image_selection == 2:
                picture_label.config(image=my_image2)
            else:
                picture_label.config(image=my_image3)

        self.root = tk.Tk()

        self.root.title("Pictures")
        self.root.geometry("800x600")

        my_image1 = ImageTk.PhotoImage(Image.open("1.bmp"))
        my_image2 = ImageTk.PhotoImage(Image.open("2.jpg"))
        my_image3 = ImageTk.PhotoImage(Image.open("3.jpeg"))

        picture_label = tk.Label(self.root, image=my_image1, justify="center")
        picture_label.pack()

        choice = tk.Entry(
            self.root,
        )
        choice.pack(padx=5, pady=5)
        button = tk.Button(self.root, text="Select Image", command=image_selector)
        button.pack(padx=5, pady=5)

        self.root.mainloop()


MyGUI()
