from abc import ABC, abstractmethod

class Animals(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def get_name(self):
        return self.name

class Dog(Animals):
    def speak(self):
        return f"Dog says Woof!"

class Cat(Animals):
    def speak(self):
        return f"Cat says Meow!"

dog = Dog("Bob")
cat = Cat("Tom")

print(dog.speak())
print(dog.get_name())
print(cat.speak())
print(cat.get_name())
