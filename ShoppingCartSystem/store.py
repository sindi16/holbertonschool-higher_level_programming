from product import Product
from user import User
class Store:
    def __init__(self):
        self.__products = [
            Product("pc", 200),
            Product("smartphone", 199)
        ]

        self.users = {}

    def register_user(self, username):
            if username in self.users:
                print("Username already exists!")
            else:
                new_user = User(username)
                self.users[username] = new_user
                print(f"User '{username}' has been registered successfully.")
                return new_user
        
    def show_products(self):
            if self.__products:
                print("Available Products:")
                for product in self.__products:
                    print(product)
                else:
                    print("No products available.")

