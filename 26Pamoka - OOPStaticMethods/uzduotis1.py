class TemperatureConverter:
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

kelvin_temperature = 300.0

celsius_temperature = TemperatureConverter.kelvin_to_celsius(kelvin_temperature)
fahrenheit_temperature = TemperatureConverter.kelvin_to_fahrenheit(kelvin_temperature)

print(f"{kelvin_temperature} Kelvins is equal to {celsius_temperature:.2f} Celsius")
print(f"{kelvin_temperature} Kelvins is equal to {fahrenheit_temperature:.2f} Fahrenheit")
