class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors

class Bike(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar

# Creating objects of Car and Bike
my_car = Car("Toyota", "Corolla", 4)
my_bike = Bike("Harley-Davidson", "Street 750", False)

# Accessing attributes
print(f"Car Brand: {my_car.brand}, Model: {my_car.model}, Doors: {my_car.number_of_doors}")
print(f"Bike Brand: {my_bike.brand}, Model: {my_bike.model}, Sidecar: {my_bike.has_sidecar}")
