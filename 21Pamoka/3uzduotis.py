class Bird:
    def speak(self):
        return "Chirp"

class Fish:
    def speak(self):
        return "Glub"

def describe_pet(pet):
    print(pet.speak())

# Testing
bird = Bird()
fish = Fish()

describe_pet(bird)  # Output: Chirp
describe_pet(fish)  # Output: Glub
