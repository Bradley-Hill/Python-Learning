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

# # Challenge 140
# def display():
#     conn = sqlite3.connect("PhoneBook.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM phonebook")
#     items = c.fetchall()
#     for item in items:
#         print(item)
#     Main()


# def Add():
#     conn = sqlite3.connect("PhoneBook.db")
#     c = conn.cursor()
#     id_number = input("Please enter the ID number: ")
#     first_name = input("Please enter the first name: ")
#     second_name = input("Please enter the second name: ")
#     phone_number = input("Please enter the phone number: ")

#     c.execute(
#         "INSERT INTO phonebook VALUES ('{}','{}','{}','{}');".format(
#             id_number, first_name, second_name, phone_number
#         )
#     )
#     conn.commit()
#     Main()


# def Search():
#     conn = sqlite3.connect("PhoneBook.db")
#     c = conn.cursor()
#     search_input = input("Please enter a second name to search for: ")
#     c.execute("SELECT * FROM phonebook WHERE second_name = '{}';".format(search_input))
#     items = c.fetchall()
#     for item in items:
#         print(item)
#     conn.commit()
#     Main()


# def Delete():
#     conn = sqlite3.connect("PhoneBook.db")
#     c = conn.cursor()
#     delete_input = input("Please enter an ID number to delete: ")
#     c.execute("DELETE from phonebook WHERE id = '{}';".format(delete_input))
#     conn.commit()
#     Main()


# def Quit():
#     return


# def Main():
#     print(
#         """
#     Main Menu

#     1)View Phonebook
#     2)Add to Phonebook
#     3)Search for Surname
#     4)Delete person from Phonebook
#     5)Quit
#     """
#     )
#     selection = int(input("Please select from the options: "))
#     while selection > 5 or selection < 1:
#         print("Please select a valid option!")
#         print(
#             """
#         Main Menu

#         1)View Phonebook
#         2)Add to Phonebook
#         3)Search for Surname
#         4)Delete person from Phonebook
#         5)Quit
#         """
#         )

#     if selection == 1:
#         display()
#     elif selection == 2:
#         Add()
#     elif selection == 3:
#         Search()
#     elif selection == 4:
#         Delete()
#     elif selection == 5:
#         Quit()


# Main()

# # Challenge 141

# conn = sqlite3.connect("BookInfo.db")

# # Create a cursor
# c = conn.cursor()
# # Create a Table
# c.execute("CREATE TABLE Authors (Name text,Place of Birth text)")

# # Commit many items into database at same time
# many_entries_authors = [
#     ("Agatha Christie", "Torquay"),
#     ("Cecelia Ahern", "Dublin"),
#     ("J.K. Rowling", "Bristol"),
#     ("Oscar Wilde", "Dublin"),
# ]

# c.executemany("INSERT INTO Authors VALUES (?,?)", many_entries_authors)
# conn.commit()

# c.execute(
#     """CREATE TABLE Books (
#     ID integer,
#     Title text,
#     Author text,
#     Date Published integer
# )"""
# )

# # Commit many items into database at same time
# many_entries_books = [
#     ("1", "De Profundis", "Oscar Wilde", "1905"),
#     ("2", "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "1998"),
#     ("3", "Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", "1999"),
#     ("4", "Lyrebird", "Cecelia Ahern", "2017"),
#     ("5", "Murder on the Orient Express", "Agatha Christie", "1934"),
#     ("6", "Perfect", "Cecelia Ahern", "2017"),
#     ("7", "The Marble Collector", "Cecelia Ahern", "2016"),
#     ("8", "The murder on the links", "Agatha Christie", "1923"),
#     ("9", "The Picture of Dorian Grey", "Oscar Wilde", "1890"),
#     ("10", "The Secret Adversary", "Agatha Christie", "1921"),
#     ("11", "The seven dials mystery", "Agatha Christie", "1929"),
#     ("12", "The year I met you", "Cecelia Ahern", "2014"),
# ]

# c.executemany("INSERT INTO Books VALUES (?,?,?,?)", many_entries_books)
# conn.commit()

# # Query the database
# c.execute("SELECT * FROM Books")
# # c.fetchone
# # c.fetchmany
# # c.fetchall()
# print(c.fetchall())

# # Commit our command
# conn.commit()

# # Close the connection
# conn.close()

# # Challenge 142

# conn = sqlite3.connect("BookInfo.db")
# c = conn.cursor()

# c.execute("SELECT * FROM Authors")
# items = c.fetchall()
# for item in items:
#     print(item)

# place_choice = input("Please enter a place of birth from the list: ")
# c.execute(
#     "SELECT Books.Title, Books.Date, Books.Author FROM Books,Authors WHERE Authors.Name = Books.Author AND authors.Place=?",
#     (place_choice,),
# )

# items2 = c.fetchall()
# for row in items2:
#     print(row)
# conn.commit()

# # Challenge 143

# conn = sqlite3.connect("BookInfo.db")
# c = conn.cursor()

# select_year = int(input("Enter a year: "))

# c.execute(
#     """SELECT Books.Title, Books.Date,Books.Author FROM Books WHERE Date>? ORDER BY Date""",
#     [select_year],
# )
# for x in c.fetchall():
#     print(x)

# Challenge 144
