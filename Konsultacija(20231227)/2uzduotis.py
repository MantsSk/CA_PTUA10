class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# Testing
student = Student("Alice", 20, "A")
print(student.name, student.age, student.grade)  # Output: Alice 20 A
