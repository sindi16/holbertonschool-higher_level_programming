from product import Product

class ShoppingCart:
    def __init__(self, items= []):
        self.__items = items

    @property
    def items(self):
        return self.__items

    def add_product(self, product):
        self.__items.append(product)

    def remove_product(self, name):
        for product in self.__items:
            if product.name == name:
                self.items.remove(product)
                return self.__items
        return "Product not found"

    def __str__(self):
        for product in self.__items:
            print(product)