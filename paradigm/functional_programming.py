from functools import reduce

items = [("A_keigen", 100), ("B", 200), ("C", 1000)]

def get_tax_rate(item_name):
    return 0.08 if item_name.endswith("_keigen") else 0.10

def calculate_price_with_tax(item):
    name, price = item
    tax_rate = get_tax_rate(name)
    return price * (1 + tax_rate)

def calculate_total(items):
    prices_with_tax = map(calculate_price_with_tax, items)
    return reduce(lambda total, price: total + price, prices_with_tax)

total_price = calculate_total(items)
print(total_price)
