class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_price_tag(self):
        print("Product:", self.name)
        print("Price: ₹" + str(self.price))


# Example
product = Product("Headphones", 2499)
product.display_price_tag()