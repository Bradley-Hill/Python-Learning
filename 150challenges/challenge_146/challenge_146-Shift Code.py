from collections import deque


def main():
    """Displays Menu choices"""
    not_quit = True
    while not_quit == True:
        print(
            """
              1)Create a coded message
              2)Decode a coded message
              3)Quit
              """
        )
        selection = int(input("Enter your selection: "))
        if selection == 1:
            code_message()
        elif selection == 2:
            decode_message()
        elif selection == 3:
            not_quit = False
            break
        else:
            print("Please enter a valid selection.")


def code_message():
    """Shift the message to new coded format"""
    user_message = input("Please enter the message you wish to be coded: ").lower()
    user_shift = int(
        input("Please enter the amount you wish the alphabet to be shifted by: ")
    )
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        " ",
    ]
    alphabet = deque(alphabet)
    alphabet.rotate(user_shift)
    shifted_alphabet = list(alphabet)
    user_shift = user_shift * -1
    alphabet.rotate(user_shift)
    shifted_alphabet = "".join(shifted_alphabet)
    alphabet = list(alphabet)
    alphabet = "".join(alphabet)
    translate_table = "".maketrans(shifted_alphabet, alphabet)
    converted_user_message = user_message.translate(translate_table)
    print(converted_user_message)
    pass


def decode_message():
    """Shift the message to new decoded format"""
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        " ",
    ]
    user_message = input("Please enter the message you want decoded: ")
    user_shift = int(
        input("Please enter the number you want to use to decode the message: ")
    )
    user_shift = user_shift * -1
    alphabet = deque(alphabet)
    alphabet.rotate(user_shift)
    shifted_alphabet = list(alphabet)
    user_shift = user_shift * -1
    alphabet.rotate(user_shift)
    shifted_alphabet = "".join(shifted_alphabet)
    alphabet = list(alphabet)
    alphabet = "".join(alphabet)
    translate_table = "".maketrans(shifted_alphabet, alphabet)
    converted_user_message = user_message.translate(translate_table)
    print(converted_user_message)
    pass


main()
