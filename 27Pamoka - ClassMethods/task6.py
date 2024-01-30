class LibrarySystem:
    def __init__(self):
        self.books = {}  # Dictionary to store book information (title: [copies_available, total_copies])
        self.users = {}  # Dictionary to store user information (user_id: [name, borrowed_books])

    def add_book(self, title, total_copies):
        # Add a book to the library system with the specified title and total number of copies
        self.books[title] = [total_copies, total_copies]

    def register_user(self, user_id, name):
        # Register a new user with the given user_id and name
        self.users[user_id] = [name, []]

    def borrow_book(self, user_id, title):
        # Allow a user to borrow a book if it's available
        if title in self.books and self.books[title][0] > 0 and user_id in self.users:
            self.books[title][0] -= 1  # Decrease available copies
            self.users[user_id][1].append(title)  # Add the borrowed book to the user's list
        else:
            print('There is no book to borrow')

    def return_book(self, user_id, title):
        # Allow a user to return a book
        if user_id in self.users and title in self.users[user_id][1]:
            self.books[title][0] += 1  # Increase available copies
            self.users[user_id][1].remove(title)  # Remove the returned book from the user's list
        else:
            print('There is no book to return')

    @classmethod
    def create_library_system(cls, user_list, book_list):
        # Class method to create a new library system instance with users and books from provided lists
        library_system = cls()
        for user_id, name in user_list:
            library_system.register_user(user_id, name)
        for title, total_copies in book_list:
            library_system.add_book(title, total_copies)
        return library_system

    @staticmethod
    def are_copies_available(books, title):
        # Static method to check if there are available copies of the specified book
        return title in books and books[title][0] > 0


# Example usage:
library = LibrarySystem()

library.add_book("Python Basics", 5)
library.add_book("Data Structures in Python", 3)

library.register_user(1, "Alice")
library.register_user(2, "Bob")

library.borrow_book(1, "Python Basics")
library.borrow_book(2, "Data Structures in Python")
library.borrow_book(2, "Python Basics")  # This should fail since there are no available copies

library.display_books()
library.display_users()

library.return_book(1, "Python Basics")
library.return_book(2, "Data Structures in Python")

library.display_books()
library.display_users()
