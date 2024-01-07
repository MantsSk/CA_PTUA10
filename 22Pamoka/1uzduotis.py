class Person:
    def __init__(self, name, age):
        self.__name = self.set_name(name)
        self.__age = self.set_age(age)
    def set_age(self, age):
        if 0 < age < 120:  # Simple validation logic
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def can_vote(self):
        return self.__age >= 18


person = Person("John", 22)
print(person.get_age())
