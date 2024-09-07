def calculate_total(items):
    total_price = 0
    for item, price in items:
        tax_rate = 0.08 if item.endswith("_keigen") else 0.10
        total_price += price * (1 + tax_rate)
    return total_price

items = [("A_keigen", 100), ("B", 200), ("C", 1000)]

total_price = calculate_total(items)
print(total_price)
