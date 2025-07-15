class ShoppingCart:
    def __init__(self):
        self.items = []  # ✅ Fixed list initialization

    def add_items(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:  # ✅ item[0], not items[0]
                self.items.remove(item)
                break  # stop after removing the first match

    def calculate_total(self) -> float:
        total = 0
        for name, qty, unit_price in self.items:
            total += qty * unit_price
        return total

    def summary(self):
        print("Cart Contents:")
        for name, qty, unit_price in self.items:
            print(f"{name}: {qty} @ Ksh{unit_price:.2f}")  # ✅ fixed variable name
        print(f"Total: Ksh{self.calculate_total():.2f}")

# ✅ Running part
if __name__ == "__main__":
    cart = ShoppingCart()  # ✅ Fixed class name (case-sensitive)

    cart.add_items("book", 2, 45.00)         # ✅ fixed function call syntax
    cart.add_items("pencils", 5, 10.00)
    cart.add_items("rubber", 1, 15.50)

    print(">>>> My Cart <<<<")
    cart.summary()
