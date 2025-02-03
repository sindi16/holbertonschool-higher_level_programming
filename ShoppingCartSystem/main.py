from product import Product
from user import User
from shoppingcart import ShoppingCart

while 1:
    print("1. Register User")
    print("2. Show Products")
    print("3. Add Product to Cart")
    print("4. View Cart")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("register user")
    elif choice == 2:
        print("show prod")
    elif choice == 3:
        print("Add prod")
    elif choice == 4:
        print("View cart")
    elif choice == 5:
        print("Bye bye")
        break
    else:
        print("Invalid choice. Press 5 if you want to exit!")

