# Import libraries 

import sqlite3
from tabulate import tabulate


class Book:
    def __init__(self, book_id, title, author, qty):
        self.Id = book_id
        self.Title = title
        self.Author = author
        self.Qty = qty

    def add_to_db(self):
        """
        Returns: A Tuple needed to add to database
        """
        return (self.Id, self.Title, self.Author, self.Qty)


# Functions outside the class

def print_table():
    """
    This function prints the list of books in the books table
    Displays the output of all rows from the books table]
    """
    results = []
    for book in cursor.execute("SELECT * FROM books"):
        results.append(book)
    print(tabulate(results, headers=["ID", "Title", "Author", "Qty"], tablefmt="sql"))


def add_book():
    """
    This function is used to add book in the database.
    Input taken from user including defensive programming Value Error.
    Creates a new_book object and adds to the database.
    Displays the new book details are added in the database.
    """
    while True:
        try:
            int_id = int(input("Enter id: "))
            qty = int(input("Enter qty: "))
            break
        except ValueError:
            print("Please only enter only integer value!")
    title = input("Title: ")
    author = input("Author: ")

# Creating new book object and adding it to the database

    new_book = Book(int_id, title, author, qty)
    cursor.execute("INSERT INTO books VALUES (?,?,?,?)", new_book.add_to_db())
    db.commit()
    print("The new book details are added to the database.")
    print_table()


def update_info():
    """
    Update the info in the books table.
    Handle the user input with defensive programming and Value Error.
    Calls def function - find_what_to_use() -> displays int value from 1 to 4 column name in books table
    Using the column number has key, find the value in the dictionary.
    Logic for user input getting new and old values to replace
    Update in the database relevant to the user's choices.
    """
    print("What do you want to update in the books detail?")

    val = find_what_to_use()

    print(f"What is the {DICT_OF_OPERATIONS[val]} you want to change to")

    while True:
        Current_value = input("Current Value: ")
        updated_value = input("Updated Value: ")
        if val == 1 or val == 4:
            try:
                updated_value = int(updated_value)
                Current_value = int(Current_value)
                break
            except ValueError:
                print("Invalid value, please try again")
        else:
            break

    if val == 1:
        cursor.execute("UPDATE books SET Id = ? WHERE Id = ?", (updated_value, Current_value))
    if val == 2:
        cursor.execute("UPDATE books SET Title = ? WHERE Title = ?", (updated_value, Current_value))
    if val == 3:
        cursor.execute("UPDATE books SET Author = ? WHERE Author = ?", (updated_value, Current_value))
    if val == 4:
        cursor.execute("UPDATE books SET Qty = ? WHERE Qty = ?", (updated_value, Current_value))
    db.commit()
    print("The records are updated successfully. Please see the updated table below:")
    print_table()


def delete_book():
    """
    Deletes the book according to the id of the book.
    Handles the user input with defensive programming and Value Error.
    Deletes sql statement using ID.
    
    """
    while True:
        try:
            id_of_book = int(input("Please enter id of book you want to delete: "))
            break
        except ValueError:
            print("Please only enter id integer value!")

    cursor.execute("DELETE FROM books WHERE Id = ?", (id_of_book,))
    db.commit()
    if cursor.rowcount == 0:
        print("The records are not found.", cursor.rowcount, "record(s) deleted")
    else:
        print(cursor.rowcount, "record(s) deleted")


def search_book():
    """
    Searching for a book.
    Handles the user input with defensive programming and Value Error.
    Calls def function - find_what_to_use() -> displays int value from 1 to 4 column name in books table
    Using the column number has key, find the value in the dictionary.
    User input to get what they are searching for. If they search on id or quantity then
    convert the value to integer.
    Search the value using if statement and displays the search result.
    
    """
    print("What do you want to search by?")

    val = find_what_to_use()

    print(f"What is the {DICT_OF_OPERATIONS[val]} you want to find?")

    while True:
        try:
            search_val = input("Enter search: ")
            if val == 1 or val == 4:
                search_val = int(search_val)
            break
        except ValueError:
            print("Please only enter a search value!")

    book_found = False
    if val == 1:
        for i in cursor.execute("SELECT * FROM books WHERE Id = ?", (search_val,)):
            print("Your book")
            print(f"--{i}--")
            book_found = True

    elif val == 2:
        for i in cursor.execute("SELECT * FROM books WHERE Title = ?", (search_val,)):
            print("Your book")
            print(f"--{i}--")
            book_found = True

    elif val == 3:
        for i in cursor.execute("SELECT * FROM books WHERE Author = ?", (search_val,)):
            print("Your book")
            print(f"--{i}--")
            book_found = True

    elif val == 4:
        for i in cursor.execute("SELECT * FROM books WHERE Qty = ?", (search_val,)):
            print("Your book")
            print(f"--{i}--")
            book_found = True

    if not book_found:
        print("--Sorry there is not a book matching that search found--")


def find_what_to_use():
    """
    Duplicate code used in search and update_info
    Handles the user input with defensive programming and Value Error to update or search.
    Display the column, 1.ID 2.Title 3.Author 4.Qty
   """
    print("1. ID\n2. Title\n3. Author\n4. Qty")
    while True:
        try:
            val = int(input(": "))
            if val in range(1, 5):
                break
            else:
                print("Enter a value from 1 to 4")
        except ValueError:
            print("Please only enter an integer value 1 to 4")
    return val


def main():
    """
    This def function will print the table initially.
    Displays the options for user input.
    Following user input, def functions are called to execute.
    Function will execute in while true loop until the user input 0-Exit to break the loop.
    
    """
    print_table()

    is_running = True
    while is_running:

# Displaying the user options

        print("\nSelect one of the following options")
        print("1. Enter book\n2. Update book\n3. Delete book\n4. Search book\n5. View all books\n0. Exit")

# Logic for user input
        while True:
            try:
                user_choice = int(input("Enter: "))
                if 0 <= user_choice < 6:
                    break
                print("Enter a valid choice 1 to 5")
            except ValueError:
                print("Please only enter a valid choice 1 to 5")

        if user_choice == 1:
            add_book()
        elif user_choice == 2:
            update_info()
        elif user_choice == 3:
            delete_book()
        elif user_choice == 4:
            search_book()
        elif user_choice == 5:
            print_table()
        elif user_choice == 0:
            is_running = False


if __name__ == '__main__':

# Setting constant dictionary for reference

    DICT_OF_OPERATIONS = {1: "Id", 2: "Title", 3: "Author", 4: "Qty"}

    try:
        db = sqlite3.connect("ebookstore.db")
        cursor = db.cursor()

# Create the table books and commit the db

        cursor.execute('''
    CREATE TABLE IF NOT EXISTS books 
    (
    Id INTEGER PRIMARY KEY, 
    Title TEXT, 
    Author TEXT, 
    Qty INTEGER
    )
    ''')
        db.commit()
        print('Created the books table successfully!')

# This is what is initially added when database is created.

        book_1 = Book(3001, "A Tale of Two Cities", "Charles Dickens", 30)
        book_2 = Book(3002, "Harry Potter and the Philosopher's Stone", "J.K Rowling", 40)
        book_3 = Book(3003, "The Lion, the Witch and the Wardrobe", "C.S Lewis", 25)
        book_4 = Book(3004, "The Lord of the Rings", "J.R.R Tolkien", 37)
        book_5 = Book(3005, "Alice in Wonderland", "Lewis Carroll", 12)

# List of book objects

        books = [
            book_1.add_to_db(),
            book_2.add_to_db(),
            book_3.add_to_db(),
            book_4.add_to_db(),
            book_5.add_to_db()
        ]
# Insert the records in the database and commit the db

        cursor.executemany("INSERT OR REPLACE INTO books VALUES (?,?,?,?)", books)
        db.commit()
        print('Inserted 5 initial records in books table successfully!')

# cursor.execute("SELECT * FROM books")
# records = cursor.fetchall()
# print(tabulate(records, headers=["ID", "Title", "Author", "Qty"], tablefmt="sql"))

        main()

# Roll back any change if something goes wrong
    
    except Exception as e:

        db.rollback()
        raise e

# Drop the books table

    finally:
        
        cursor.execute('''DROP TABLE books''')
        db.commit()
        print("\nDrop the table books to re-execute the code without error")
        db.close()
        print("DB Connection is closed")
  
