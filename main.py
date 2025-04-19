from transaction import Transaction  # Import the Transaction class from the transaction module
from tabulate import tabulate        # Import tabulate to display cart as table

# Create a transaction object – this is where we store the cart data
transaction = Transaction()

# This function shows the list of actions the user can perform
def show_menu():
    print("""
========= Super Cashier Menu =========
1. Add Item
2. Update Item Name
3. Update Item Quantity
4. Update Item Price
5. Delete Item
6. Reset Cart
7. Show Cart
8. Calculate Total Price
9. Exit
""")

# This is the main loop – it runs until the user chooses to exit
while True:
    show_menu()
    choice = input("Please select an option (1-9): ")

    if choice == '1':
        # Add a new item
        item_name = input("Enter item name: ")
        try:
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter price per item: "))
            transaction.add_item([item_name, quantity, price])
        except ValueError:
            print("Invalid input. Quantity and price must be numbers.")

    elif choice == '2':
        # Update an item's name
        old_name = input("Enter current item name: ")
        new_name = input("Enter new item name: ")
        transaction.update_item_name(old_name, new_name)

    elif choice == '3':
        # Update quantity of an item
        item_name = input("Enter item name: ")
        try:
            new_quantity = int(input("Enter new quantity: "))
            transaction.update_item_quantity(item_name, new_quantity)
        except ValueError:
            print("Invalid input. Quantity must be a number.")

    elif choice == '4':
        # Update price of an item
        item_name = input("Enter item name: ")
        try:
            new_price = int(input("Enter new price: "))
            transaction.update_item_price(item_name, new_price)
        except ValueError:
            print("Invalid input. Price must be a number.")

    elif choice == '5':
        # Delete an item
        item_name = input("Enter item name to delete: ")
        transaction.delete_item(item_name)

    elif choice == '6':
        # Reset the entire cart
        transaction.reset_cart()

    elif choice == '7':
        # Show all items in the cart
        transaction.check_order()

    elif choice == '8':
        # Calculate the total price (with discount if any)
        transaction.total_price()

    elif choice == '9':
        # Exit the program
        print("Thank you for using Super Cashier. Goodbye!")
        break

    else:
        # Handle invalid menu option
        print("Invalid choice. Please select a number from 1 to 9.")
