class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        # Call the constructor of the parent class (Person) to handle name and age
        super().__init__(name, age)
        self.grade = grade

# Example usage:
person1 = Person("John", 25)
print("Person:", person1.name, person1.age)

student1 = Student("Alice", 20, "A")
print("Student:", student1.name, student1.age, student1.grade)
