class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected attribute

    def get_age(self):
        return self._age

    def update_age(self, new_age):
        if 18 <= new_age <= 30:
            self._age = new_age
        else:
            print("Invalid age range. Age not updated.")

# Usage
student1 = Student("Alice", 20)
print(f"Before update: {student1.name}'s age is {student1.get_age()}")
student1.update_age(35)
print(f"After update: {student1.name}'s age is {student1.get_age()}")