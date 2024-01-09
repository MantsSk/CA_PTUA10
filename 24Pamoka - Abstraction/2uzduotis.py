from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, currency, value):
        self.currency = currency
        self.value = value

    def get_value(self):
        return self.value

    def get_currency(self):
        return self.currency

    @abstractmethod
    def convert_to_currency(self, target_currency, conversion_rate):
        pass


class Cash(Money):
    def __init__(self, currency, value, denomination):
        super().__init__(currency, value)
        self.denomination = denomination

    def convert_to_currency(self, target_currency, conversion_rate):
        self.value = round(self.value * conversion_rate[self.currency] * conversion_rate[target_currency], 2)
        self.currency = target_currency
        for _ in range(int(self.value / self.denomination)):
            self.value -= self.denomination


class Card(Money):
    def __init__(self, currency, value, credit_limit):
        super().__init__(currency, value)
        self.credit_limit = credit_limit

    def convert_to_currency(self, target_currency, conversion_rate):
        self.value = round(
            min(self.value, self.credit_limit) * conversion_rate[self.currency] * conversion_rate[target_currency], 2)
        self.currency = target_currency


rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
}

# Create a Cash object with initial value and denomination
cash = Cash("USD", 100.0, 20)

# Convert the Cash object to EUR
cash.convert_to_currency("EUR", rates)

print(f"Converted Cash value: {cash.get_value()} {cash.get_currency()}")  # Output: Converted Cash value: 85.0 EUR

# Create a Card object with initial value and credit limit
card = Card("EUR", 500.0, 1000.0)

# Convert the Card object to GBP
card.convert_to_currency("GBP", rates)

print(f"Converted Card value: {card.get_value()} {card.get_currency()}")  # Output: Converted Card value: 375.0 GBP
