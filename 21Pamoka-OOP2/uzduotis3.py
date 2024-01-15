class Bird:
    def speak(self):
        return "Tweet!"

class Fish:
    def speak(self):
        return "Bubble bubble!"

def describe_pet(animal):
    print(f"The pet says: {animal.speak()}")

# Demonstrate polymorphism
bird_instance = Bird()
fish_instance = Fish()

describe_pet(bird_instance)
describe_pet(fish_instance)
