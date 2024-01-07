import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Using the classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle area:", circle.area())        # Output: Area of the circle
print("Rectangle area:", rectangle.area())  # Output: Area of the rectangle
