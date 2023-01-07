import sqlite3

# # Challenge 139
# conn = sqlite3.connect("PhoneBook.db")

# # Create a cursor
# c = conn.cursor()
# # Create a Table
# # c.execute(
# #     """CREATE TABLE phonebook (
# #     id integer,
# #     first_name text,
# #     second_name text,
# #     phone_number integer
# # )"""
# # )
# # Same code but harder to read all on one line.
# # c.execute("CREATE TABLE phonebook (id INTEGER,first_name TEXT,second_name TEXT,phone_number INTEGER)")

# # Single item entry to database
# # c.execute("INSERT INTO phonebook VALUES ('2','Karen','Phillips','01954 295773')")


# # Commit many items into database at same time
# # many_entries = [
# #     ("1", "Simon", "Howels", "01223 349752"),
# #     ("2", "Karen", "Phillips", "01954 29773"),
# #     ("3", "Darren", "Smith", "01583 749012"),
# #     ("4", "Anne", "Jones", "01323 567322"),
# #     ("5", "Mark", "Smith", "01223 855534"),
# # ]

# # c.executemany("INSERT INTO phonebook VALUES (?,?,?,?)", many_entries)

# # Query the database
# c.execute("SELECT * FROM phonebook")
# # c.fetchone
# # c.fetchmany
# # c.fetchall()
# print(c.fetchall())

# # Commit our command
# conn.commit()

# # Close the connection
# conn.close()

# Challenge 140
def display():
    conn = sqlite3.connect("PhoneBook.db")
    c = conn.cursor()
    c.execute("SELECT * FROM phonebook")
    items = c.fetchall()
    for item in items:
        print(item)
    Main()


def Add():
    conn = sqlite3.connect("PhoneBook.db")
    c = conn.cursor()
    id_number = input("Please enter the ID number: ")
    first_name = input("Please enter the first name: ")
    second_name = input("Please enter the second name: ")
    phone_number = input("Please enter the phone number: ")

    c.execute(
        "INSERT INTO phonebook VALUES ('{}','{}','{}','{}');".format(
            id_number, first_name, second_name, phone_number
        )
    )
    conn.commit()
    Main()


def Search():
    conn = sqlite3.connect("PhoneBook.db")
    c = conn.cursor()
    search_input = input("Please enter a second name to search for: ")
    c.execute("SELECT * FROM phonebook WHERE second_name = '{}';".format(search_input))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    Main()


def Delete():
    conn = sqlite3.connect("PhoneBook.db")
    c = conn.cursor()
    delete_input = input("Please enter an ID number to delete: ")
    c.execute("DELETE from phonebook WHERE id = '{}';".format(delete_input))
    conn.commit()
    Main()


def Quit():
    return


def Main():
    print(
        """
    Main Menu
        
    1)View Phonebook
    2)Add to Phonebook
    3)Search for Surname
    4)Delete person from Phonebook
    5)Quit
    """
    )
    selection = int(input("Please select from the options: "))
    while selection > 5 or selection < 1:
        print("Please select a valid option!")
        print(
            """
        Main Menu
        
        1)View Phonebook
        2)Add to Phonebook
        3)Search for Surname
        4)Delete person from Phonebook
        5)Quit
        """
        )

    if selection == 1:
        display()
    elif selection == 2:
        Add()
    elif selection == 3:
        Search()
    elif selection == 4:
        Delete()
    elif selection == 5:
        Quit()


Main()


# while selection > 5 or selection < 1:
#     print("Please select a valid option!")
#     print(
#         """
#       Main Menu

#       1)View Phonebook
#       2)Add to Phonebook
#       3)Search for Surname
#       4)Delete person from Phonebook
#       5)Quit
#       """
#     )
#     selection = int(input("Please select from the options: "))
# if selection == 1:
#     display()
# elif selection == 2:
#     Add()
# elif selection == 3:
#     Search()
# elif selection == 4:
#     Delete()
# elif selection == 5:
#     Quit()
