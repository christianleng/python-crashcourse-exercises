from forex_python.converter import CurrencyRates

cr = CurrencyRates()

amount = int(input("Enter the amount: "))
from_currency = input("Source currency (USD/EUR/CAD): ").upper()
to_currency = input("Target currency (USD/EUR/CAD): ").upper()


output = cr.convert(from_currency, to_currency, amount)

print(amount, from_currency, "is equal to", output, to_currency)
