class Item:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_details(self):
        return f"Title: {self.__title}, Author: {self.__author}"

class Book(Item):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.__page_count = page_count

    def get_page_count(self):
        return self.__page_count

    def set_page_count(self, page_count):
        self.__page_count = page_count

    def get_details(self):
        return f"{super().get_details()}, Page Count: {self.__page_count}"

class DVD(Item):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_details(self):
        return f"{super().get_details()}, Duration: {self.__duration} minutes"

class Journal(Item):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        self.__issue_number = issue_number

    def get_details(self):
        return f"{super().get_details()}, Issue Number: {self.__issue_number}"

# Using the classes
book = Book("1984", "George Orwell", 328)
dvd = DVD("Inception", "Christopher Nolan", 148)
journal = Journal("Nature", "Various Authors", "Vol. 49 No. 3")

print(book.get_details())
print(dvd.get_details())
print(journal.get_details())
