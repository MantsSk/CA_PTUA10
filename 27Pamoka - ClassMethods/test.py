class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"
    
    def __len__(self):
        return 2

p1 = Product("Apple", 0.5)
p2 = Product("Apple", 0.5)
print(p1 == p2)  # Product: Apple, Price: 0.5
print(repr(p1)) # Product('Apple', 0.5)

print(len(p1))
