class Shape:
    def __init__(self, width, height):
        self._width = width  # Protected attribute
        self._height = height  # Protected attribute

    def calculate_area(self):
        return self._width * self._height

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
        
    def calculate_area(self):
        self._width = 10
        return super().calculate_area()

# Example usage:
rectangle = Rectangle(4, 6)
print(rectangle)
print(rectangle.calculate_area())  # Output: 24
