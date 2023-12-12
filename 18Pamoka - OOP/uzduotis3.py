class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return "Title: " + self.title

    def get_author(self):
        return "Author: " + self.author

PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")

print(PP.title)  # Output: "Pride and Prejudice"
print(PP.author)  # Output: "Jane Austen"
print(PP.get_title())  # Output: "Title: Pride and Prejudice"
print(PP.get_author())  # Output: "Author: Jane Austen"
