import sqlite3

# Challenge 139
conn = sqlite3.connect("PhoneBook.db")

# Create a cursor
c = conn.cursor()
# Create a Table
c.execute(
    """CREATE TABLE phonebook (
    id integer,
    first_name text,
    second_name text,
    phone_number integer
)"""
)
# Same code but harder to read all on one line.
# c.execute("CREATE TABLE phonebook (id INTEGER,first_name TEXT,second_name TEXT,phone_number INTEGER)")

# Commit our command
conn.commit()

# Close the connection
conn.close()
