class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

    def read_book(self):
        if self.is_available:
            print(f"Reading '{self.title}' by {self.author}...")
        else:
            print(f"The book '{self.title}' is currently not available.")

    def change_availability(self, available):
        self.is_available = available
        status = "available" if available else "not available"
        print(f"The book '{self.title}' is now {status}.")

# Example of using the Book class
my_book = Book("1984", "George Orwell")
my_book.display_info()
my_book.read_book()
my_book.change_availability(False)
my_book.read_book()
