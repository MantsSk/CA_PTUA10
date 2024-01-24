class ReadOnlyProperty:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

# Example Usage
read_only = ReadOnlyProperty("This is read-only")

read_only.value = "Whats going on?" # property 'value' of 'ReadOnlyProperty' object has no setter
