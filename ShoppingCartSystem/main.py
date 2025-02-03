from product import Product
from user import User
from shoppingcart import ShoppingCart
from store import Store

clothes_store = Store()
cart = ShoppingCart()



while 1:
    print("1. Register User")
    print("2. Show Products")
    print("3. Add Product to Cart")
    print("4. View Cart")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("please enter your username: ")
        clothes_store.register_user(username)
    
    elif choice == 2:
        
    elif choice == 3:
        print("Add prod")
    elif choice == 4:
        print("View cart")
    elif choice == 5:
        print("Bye bye")
        break
    else:
        print("Invalid choice. Press 5 if you want to exit!")
