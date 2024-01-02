class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Testing
dog = Dog()
print(dog.speak())  # Output: Woof

cat = Cat()
print(cat.speak())  # Output: Meow
