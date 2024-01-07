class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"Bark! My name is {self.name}."

class Cat(Animal):
    def make_sound(self):
        return f"Meow! My name is {self.name}."

class Bird(Animal):
    def make_sound(self):
        return f"Tweet! My name is {self.name}."

    def fly(self):
        return f"{self.name} is flying high!"

# Using the classes
dog = Dog("Rex")
cat = Cat("Whiskers")
bird = Bird("Sky")

print(dog.make_sound())    # Output: "Bark! My name is Rex."
print(cat.make_sound())    # Output: "Meow! My name is Whiskers."
print(bird.make_sound())   # Output: "Tweet! My name is Sky."
print(bird.fly())          # Output: "Sky is flying high!"
