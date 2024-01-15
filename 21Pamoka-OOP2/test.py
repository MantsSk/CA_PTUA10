class Shape:
    def __init__(self, width, height):
        self._width = width  # Protected attribute
        self._height = height  # Protected attribute

    def calculate_area(self):
        return self._width * self._height

class Rectangle(Shape):
    def calculate_area(self):
        return super().calculate_area()

# Example usage:
rectangle = Rectangle(4, 6)
print(rectangle.calculate_area())  # Output: 24
