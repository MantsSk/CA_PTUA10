class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 20000000 or self.area > 3000000
        self.population_density = self.population / self.area

    def compare_population_density(self, other_country):
        if self.population_density > other_country.population_density:
            return f"{self.name} has a larger population density than {other_country.name}"
        elif self.population_density < other_country.population_density:
            return f"{self.name} has a smaller population density than {other_country.name}"
        else:
            return f"{self.name} and {other_country.name} have the same population density"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)  
print(andorra.is_big)   
print(andorra.compare_population_density(australia))
