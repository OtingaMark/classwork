class ShoppingCart:
    def __init__(self):
        self.items = []  # Initialize an empty list to store (item_name, qty) tuples

    def add_item(self, item_name: str, qty: int):
        self.items.append((item_name, qty))  # Add item to the list

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break  # Stop after removing the first match

    def display_items(self):
        if not self.items:
            print("Cart is empty.")
        else:
            for name, qty in self.items:
                print(f"{name}: {qty}")

# --- Using the class properly ---
cart = ShoppingCart()
cart.add_item("Papaya", 9)
cart.add_item("Guava", 17)

print("Shopping Cart Contents:")
cart.display_items()

cart.remove_item("Papaya")
print("\nAfter removing Papaya:")
cart.display_items()
