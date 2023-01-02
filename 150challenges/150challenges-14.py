import tkinter as tk
from tkinter import messagebox
import random

## Challenge 124
# class MyGUI:
#     def __init__(self) -> None:

#         self.root = tk.Tk()

#         self.label = tk.Label(self.root, text="Enter your name!", font=("Arial", 18))
#         self.label.pack(padx=10, pady=10)

#         self.textbox = tk.Text(self.root, height=3, font=("Arial", 15))
#         self.textbox.pack(padx=10, pady=10)

#         self.check_state = tk.IntVar()

#         self.check = tk.Checkbutton(
#             self.root,
#             text="Click Here",
#             font=("Arial", 15),
#             variable=self.check_state,
#         )
#         self.check.pack(padx=10, pady=10)

#         self.button = tk.Button(
#             self.root,
#             text="Display Message",
#             font=("Arial", 18),
#             command=self.show_message,
#         )
#         self.button.pack(padx=10, pady=10)

#         self.root.mainloop()

#     def show_message(self):
#         if self.check_state.get() == 0:
#             print("Hello, ", (self.textbox.get("1.0", tk.END)))
#         else:
#             messagebox.showinfo(
#                 title="Message", message="Hello, " + self.textbox.get("1.0", tk.END)
#             )


# MyGUI()

## Challenge 125
# def dice_roll():
#     num = random.randint(1, 6)
#     answer["text"] = num


# root = tk.Tk()

# root.geometry("600x600")
# root.title("Dice Roll")

# label = tk.Label(root, text="Roll the die!", font=("Arial", 18))
# label.pack(padx=10, pady=10)

# button = tk.Button(
#     root, text="Press here to Roll.", font=("Arial", 14), command=dice_roll
# )
# button.pack(padx=20, pady=20)

# answer = tk.Message(root, text="")
# answer.pack(padx=30, pady=30)

# root.mainloop()
# Challenge 126
# def Add():
#     num = entry_box.get()
#     num = int(num)
#     output_txt = total
#     answer = output_txt
#     answer = int(answer)
#     total = num + answer


# def reset():
#     total = 0
#     output_txt = 0
#     entry_box.delete("1.0", tk.END)


class MyGui:
    def __init__(self) -> None:

        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title("Adding numbers")

        self.label = tk.Label(
            self.root, text="Enter a number to add.", font=("Arial", 18)
        )
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root, height=1, font=("Arial", 14))
        self.textbox.pack(padx=20, pady=20)

        self.button1 = tk.Button(
            self.root, text="Add a number", font=("Arial", 14), command=self.Addition
        )
        self.button1.pack(padx=10, pady=10)
        self.button2 = tk.Button(
            self.root, text="Reset count.", font=("Arial", 14), command=self.Reset
        )
        self.button2.pack(padx=10, pady=10)

        self.messagebox = tk.Message(
            self.root, text="", font=("Arial", 18), fg="blue", bg="white"
        )
        self.messagebox.pack(padx=35, pady=35)

        self.root.mainloop()

    def Addition(self):
        num = self.textbox.get("1.0", "end-1c")
        num = int(num)

    def Reset(self):
        print("poop")


MyGui()


# root = tk.Tk()

# root.geometry("500x500")
# root.title("Adding together")

# entry_box = tk.Entry(
#     root,
#     textvariable="",
# )
# entry_box.pack(padx=20, pady=20)

# button1 = tk.Button(root, text="Add the number to the total", command=Add)
# button1.pack(padx=20, pady=20)

# button2 = tk.Button(root, text="Reset", command=reset)
# button2.pack(padx=20, pady=20)

# output_txt = tk.Message(root, text="")
# output_txt.pack(padx=30, pady=30)

# root.mainloop()
