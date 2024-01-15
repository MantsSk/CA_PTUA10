class ImperialToMetricConverter:
    @staticmethod
    def inches_to_centimeters(inches):
        return inches * 2.54

    @staticmethod
    def feet_to_meters(feet):
        return feet * 0.3048

    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds * 0.453592

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934

length_inches = 10.0
length_feet = 5.0
weight_pounds = 150.0
temperature_fahrenheit = 68.0
distance_miles = 20.0

converted_length_cm = ImperialToMetricConverter.inches_to_centimeters(length_inches)
converted_length_meters = ImperialToMetricConverter.feet_to_meters(length_feet)
converted_weight_kg = ImperialToMetricConverter.pounds_to_kilograms(weight_pounds)
converted_temperature_celsius = ImperialToMetricConverter.fahrenheit_to_celsius(temperature_fahrenheit)
converted_distance_km = ImperialToMetricConverter.miles_to_kilometers(distance_miles)

print(f"{length_inches} inches is equal to {converted_length_cm:.2f} centimeters")
print(f"{length_feet} feet is equal to {converted_length_meters:.2f} meters")
print(f"{weight_pounds} pounds is equal to {converted_weight_kg:.2f} kilograms")
print(f"{temperature_fahrenheit} Fahrenheit is equal to {converted_temperature_celsius:.2f} Celsius")
print(f"{distance_miles} miles is equal to {converted_distance_km:.2f} kilometers")
