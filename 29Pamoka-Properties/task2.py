class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # Protected attribute

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if -273.15 <= value:
            self._celsius = value
        else:
            raise ValueError("Temperature below absolute zero is not possible")

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Example Usage
temp = Temperature()
temp.celsius = 25
print(temp.fahrenheit)  # Output: 77.0
temp.fahrenheit = 32
print(temp.celsius)  # Output: 0.0
