class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__salary = 0  # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

# Example usage:
employee = Employee("John Doe", 30)
employee.set_salary(50000)
print(f"Name: {employee.get_name()}, Age: {employee.get_age()}, Salary: {employee.get_salary()}")  # Output: Name: John Doe, Age: 30, Salary: 50000
