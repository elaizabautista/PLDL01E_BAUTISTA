from abc import ABC, abstractmethod


# Abstract class Product
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_info(self):
        pass


# Subclass Electronics
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def get_info(self):
        return f"{self.name} (₱{self.price}) - Warranty: {self.warranty} year(s)"


# Subclass Clothing
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_info(self):
        return f"{self.name} (₱{self.price}) - Size: {self.size}"


# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add(self, product):
        self.cart.append(product)
        print(f"Added: {product.get_info()}")

    def view(self):
        print("\nShopping Cart:" if self.cart else "Cart is empty.")
        for i, product in enumerate(self.cart, 1):
            print(f"{i}. {product.get_info()}")

    def checkout(self):
        print(f"\nTotal: ₱{sum(p.price for p in self.cart):.2f}")


# Test
e1, e2 = Electronics("Laptop", 50000, 2), Electronics("Smartphone", 30000, 1)
c1, c2 = Clothing("T-Shirt", 500, "M"), Clothing("Jeans", 1500, "L")
cart = ShoppingCart()
for item in [e1, e2, c1, c2]: cart.add(item)
cart.view()
cart.checkout()
