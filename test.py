class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def __iadd__(self, item):
        """Add item to cart (in-place)"""
        if isinstance(item, str):
            self.items.append(item)
            print(f"Added '{item}' to cart")
        elif isinstance(item, list):
            self.items.extend(item)
            print(f"Added multiple items to cart")
        else:
            raise TypeError("Can only add strings or lists to cart")
        return self
    
    def __repr__(self):
        return f"ShoppingCart({self.items})"

# Using += with ShoppingCart
cart = ShoppingCart()
print("Empty cart:", cart)  # ShoppingCart([])

# Add single item
cart += "Apple"
# Output: Added 'Apple' to cart
print("After adding apple:", cart)  # ShoppingCart(['Apple'])

# Add multiple items
cart += ["Banana", "Orange"]
# Output: Added multiple items to cart
print("After adding fruits:", cart)  # ShoppingCart(['Apple', 'Banana', 'Orange'])

# Chain additions
cart += "Milk""Bread"
print("Final cart:", cart)  # ShoppingCart(['Apple', 'Banana', 'Orange', 'Milk', 'Bread'])