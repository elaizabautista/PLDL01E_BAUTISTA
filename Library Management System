#create a class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

# Add books to the library
library = Library()
library.add_book(Book("Pride and Prejudice", "Jane Austen", "1111111111"))
library.add_book(Book("The Notebook", "Nicholas Sparks", "2222222222"))
library.add_book(Book("Me Before You", "Jojo Moyes", "3333333333"))

# Main menu loop
while True:
    print("\n1. Show Books  2. Borrow Book  3. Return Book  4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        title = input("Enter book title to borrow: ")
        book = library.search_book(title)
        if book and book.borrow_book():
            print(f"You borrowed '{title}'.")
        else:
            print("Book not available or not found.")
    elif choice == "3":
        title = input("Enter book title to return: ")
        book = library.search_book(title)
        if book:
            book.return_book()
            print(f"You returned '{title}'.")
        else:
            print("Book not found.")
    elif choice == "4":
        break
    else:
        print("Invalid option. Try again.")
