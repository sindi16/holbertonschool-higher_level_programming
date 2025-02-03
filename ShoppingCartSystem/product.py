class Product:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("Price must be more than 0")
        self.__name = name
        self.__price = price
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

    def __dict__(self):
        return {
            "name": self.__name,
            "price": self.__price
        }