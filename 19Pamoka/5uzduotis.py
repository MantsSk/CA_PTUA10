class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book}' has been added to the library.")

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.borrowed_books[book] = True
            print(f"'{book}' has been borrowed.")
        else:
            print(f"Sorry, '{book}' is not available or already borrowed.")

    def return_book(self, book):
        if self.borrowed_books.get(book):
            self.books.append(book)
            del self.borrowed_books[book]
            print(f"'{book}' has been returned.")
        else:
            print(f"'{book}' was not borrowed from this library.")

    def display_available_books(self):
        if self.books:
            print("Available Books:")
            for book in self.books:
                print(book)
        else:
            print("No books are currently available.")

# Example of using the Library class
my_library = Library()
my_library.add_book("1984")
my_library.add_book("To Kill a Mockingbird")
my_library.display_available_books()
my_library.borrow_book("1984")
my_library.display_available_books()
my_library.return_book("1984")
my_library.display_available_books()
