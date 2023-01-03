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
# # Challenge 126


# class MyGui:
#     def __init__(self) -> None:

#         self.runningTotal = 0

#         self.root = tk.Tk()

#         self.root.geometry("500x500")
#         self.root.title("Adding numbers")

#         self.label = tk.Label(
#             self.root, text="Enter a number to add.", font=("Arial", 18)
#         )
#         self.label.pack(padx=20, pady=20)

#         self.textbox = tk.Text(self.root, height=1, font=("Arial", 14))
#         self.textbox.pack(padx=20, pady=20)

#         self.button1 = tk.Button(
#             self.root, text="Add a number", font=("Arial", 14), command=self.Addition
#         )
#         self.button1.pack(padx=10, pady=10)
#         self.button2 = tk.Button(
#             self.root, text="Reset count.", font=("Arial", 14), command=self.Reset
#         )
#         self.button2.pack(padx=10, pady=10)

#         self.running_total = tk.Label(
#             self.root, text=str(self.runningTotal), font=("Arial", 24)
#         )
#         self.running_total.pack(padx=25, pady=25)

#         self.root.mainloop()

#     def Addition(self):
#         num = self.textbox.get("1.0", "end-1c")
#         num = int(num)
#         self.runningTotal += num
#         self.running_total.config(text=str(self.runningTotal))
#         print(self.runningTotal)

#     def Reset(self):
#         self.runningTotal = 0
#         self.running_total.config(text=str(self.runningTotal))


# MyGui()

# # Challenge 127


# class MyGui:
#     def __init__(self) -> None:

#         self.list = ""

#         self.root = tk.Tk()

#         self.root.geometry("500x500")
#         self.root.title("Adding names")

#         self.label = tk.Label(
#             self.root, text="Enter a name to add.", font=("Arial", 18)
#         )
#         self.label.pack(padx=20, pady=20)

#         self.textbox = tk.Text(self.root, height=1, font=("Arial", 14))
#         self.textbox.pack(padx=20, pady=20)

#         self.button1 = tk.Button(
#             self.root, text="Add a name", font=("Arial", 14), command=self.Addition
#         )
#         self.button1.pack(padx=10, pady=10)
#         self.button2 = tk.Button(
#             self.root, text="Reset list.", font=("Arial", 14), command=self.Reset
#         )
#         self.button2.pack(padx=10, pady=10)

#         self.running_total = tk.Label(
#             self.root, text=str(self.list), font=("Arial", 24)
#         )
#         self.running_total.pack(padx=25, pady=25)

#         self.root.mainloop()

#     def Addition(self):
#         name = self.textbox.get("1.0", "end-1c")
#         name = str(name) + "\n"
#         self.list += name
#         self.running_total.config(text=str(self.list))
#         print(self.list)

#     def Reset(self):
#         self.list = ""
#         self.running_total.config(text=str(self.list))


# MyGui()

# Challenge 128
class MyGui:
    def __init__(self) -> None:

        self.conversion = 0

        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title("Converting between Miles and Kilometres")

        self.label = tk.Label(
            self.root, text="Enter a number to add.", font=("Arial", 18)
        )
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root, height=1, font=("Arial", 14))
        self.textbox.pack(padx=20, pady=20)

        self.button1 = tk.Button(
            self.root,
            text="Convert to Kms",
            font=("Arial", 14),
            command=self.Kilometres,
        )
        self.button1.pack(padx=10, pady=10)
        self.button2 = tk.Button(
            self.root, text="Convert to Miles.", font=("Arial", 14), command=self.Miles
        )
        self.button2.pack(padx=10, pady=10)

        self.output = tk.Label(self.root, text=str(self.conversion), font=("Arial", 24))
        self.output.pack(padx=25, pady=25)

        self.root.mainloop()

    def Kilometres(self):
        num = self.textbox.get("1.0", "end-1c")
        pass

    def Miles(self):
        num = self.textbox.get("1.0", "end-1c")
        pass


MyGui()
