class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage:
generic_animal = Animal()
print("Generic Animal:", generic_animal.speak())

dog = Dog()
print("Dog:", dog.speak())

cat = Cat()
print("Cat:", cat.speak())