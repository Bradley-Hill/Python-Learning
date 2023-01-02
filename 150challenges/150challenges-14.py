import tkinter as tk
from tkinter import messagebox

# Challenge 124
class MyGUI:
    def __init__(self) -> None:

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Enter your name!", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3, font=("Arial", 15))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(
            self.root,
            text="Click Here",
            font=("Arial", 15),
            variable=self.check_state,
        )
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(
            self.root,
            text="Display Message",
            font=("Arial", 18),
            command=self.show_message,
        )
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print("Hello, ", (self.textbox.get("1.0", tk.END)))
        else:
            messagebox.showinfo(
                title="Message", message="Hello, " + self.textbox.get("1.0", tk.END)
            )


MyGUI()


# root = tk.Tk()
# root.geometry("800x600")
# root.title("My First GUI")

# label = tk.Label(root, text="Please enter your name...", font=("Arial", 18))
# label.pack(padx=20, pady=20)

# entrybox = tk.Entry(root, font=("Arial", 13))
# entrybox.pack(padx=15)

# button = tk.Button(root, text="Click Here", font=("Arial", 18))
# button.pack(padx=20, pady=20)

# root.mainloop()
