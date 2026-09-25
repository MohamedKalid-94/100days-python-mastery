# Day 23 - Library Management System
# Concept: Constructors & Methods
# Goal: Practice building out a constructor properly and writing useful methods

class Book:

    # --- Constructor with default parameter values ---
    # If 'is_borrowed' isn't provided, it defaults to False
    def __init__(self, title, author, isbn, is_borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    # --- A method that CHANGES the object's state ---
    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'.")

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed.")
        else:
            self.is_borrowed = False
            print(f"You returned '{self.title}'.")

    # --- A method that RETURNS a value instead of printing ---
    def get_status(self):
        return "Borrowed" if self.is_borrowed else "Available"

    # --- __str__ controls how the object looks when printed ---
    def __str__(self):
        return f"'{self.title}' by {self.author} - {self.get_status()}"


class Library:

    # --- A constructor that sets up an internal list to track state ---
    def __init__(self, name):
        self.name = name
        self.books = []   # each Library object starts with its own empty list

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to {self.name}.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None   # not found

    def show_all_books(self):
        print(f"\n--- Books in {self.name} ---")
        if not self.books:
            print("No books yet.")
        for book in self.books:
            print(book)   # this calls __str__ on each book automatically

    def show_available_books(self):
        available = [book for book in self.books if not book.is_borrowed]
        print(f"\n--- Available books in {self.name} ---")
        for book in available:
            print(book)


# --- Creating Book objects using the constructor ---
book1 = Book("The Hobbit", "J.R.R. Tolkien", "1234567890")
book2 = Book("Dune", "Frank Herbert", "2345678901")
book3 = Book("1984", "George Orwell", "3456789012", is_borrowed=True)   # using the default override

# --- print() now shows something useful, thanks to __str__ ---
print(book1)
print(book2)
print(book3)

# --- Creating a Library object and adding books to it ---
my_library = Library("City Library")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.show_all_books()

# --- Calling methods that change state ---
book1.borrow()
book1.borrow()   # trying again - shows the "already borrowed" message

my_library.show_available_books()

book1.return_book()
my_library.show_available_books()

# --- Using a method that RETURNS a value ---
status = book2.get_status()
print(f"\nDune's status: {status}")

# --- Finding a book and using isinstance() to confirm its type ---
found_book = my_library.find_book("Dune")
if found_book:
    print(f"\nFound: {found_book}")
    print("Is it a Book object?", isinstance(found_book, Book))


# ============================================================
# Interactive part: manage the library yourself
# ============================================================
print("\n--- Library Management System ---")
while True:
    print("\n1. Show all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Add a new book")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        my_library.show_all_books()
    elif choice == "2":
        title = input("Enter the title to borrow: ")
        book = my_library.find_book(title)
        if book:
            book.borrow()
        else:
            print("Book not found.")
    elif choice == "3":
        title = input("Enter the title to return: ")
        book = my_library.find_book(title)
        if book:
            book.return_book()
        else:
            print("Book not found.")
    elif choice == "4":
        new_title = input("Title: ")
        new_author = input("Author: ")
        new_isbn = input("ISBN: ")
        my_library.add_book(Book(new_title, new_author, new_isbn))
    elif choice == "5":
        break
    else:
        print("Invalid option.")

print("\nGoodbye!")