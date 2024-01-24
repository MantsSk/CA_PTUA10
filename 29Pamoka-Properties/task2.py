class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self.celsius * 1.8) + 32

t = Temperature(20)
t.celsius = 20
print(t.celsius)
print(t.fahrenheit)
