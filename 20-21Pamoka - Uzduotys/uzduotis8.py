class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        print(f"Books available in {self.name}:")
        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' by {self.author} checked out successfully.")
        else:
            print(f"Book '{self.title}' by {self.author} is currently not available.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book '{self.title}' by {self.author} returned.")
        else:
            print(f"Book '{self.title}' by {self.author} was not checked out.")

# Usage
library = Library("City Library")

library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")

library.display_books()

book_to_check_out = library.books[0]
book_to_check_out.check_out()

library.display_books()

book_to_check_out.return_book()

library.display_books()

