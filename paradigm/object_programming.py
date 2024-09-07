class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_tax_rate(self):
        if self.name.endswith("_keigen"):
            return 0.08
        else:
            return 0.10

    def get_price_with_tax(self):
        tax_rate = self.get_tax_rate()
        return self.price * (1 + tax_rate)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_price_with_tax()
        return total


item1 = Item("A_keigen", 100)
item2 = Item("B", 200)
item3 = Item("C", 1000)

cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

total_price = cart.calculate_total()
print(total_price)
