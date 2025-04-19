from tabulate import tabulate

class Transaction:
    """
    A class that manages a customer's shopping cart in the Super Cashier program.
    """

    def __init__(self):
        """
        Create an empty dictionary to store all shopping items.
        Format:
        {
            "item_name": [quantity, price_per_item]
        }
        """
        self.cart = {}

    def add_item(self, details):
        """
        Add a new item or increase quantity in the cart.

        Parameters:
        - details: list of [item_name, quantity, price_per_item]
        """
        try:
            item_name = details[0]
            quantity = int(details[1])
            price = int(details[2])

            if item_name in self.cart:
                self.cart[item_name][0] += quantity  # add quantity if item already exists
                self.cart[item_name][1] = price      # update the latest price
            else:
                self.cart[item_name] = [quantity, price]

            # ✅ NEW OUTPUT MESSAGE (grammar-aware)
            print(f"Item{'s' if quantity > 1 else ''} bought: {item_name} (Qty: {quantity}) at Rp {price:,} each.")

        except Exception as e:
            print("Invalid input data:", e)

    def update_item_name(self, old_name, new_name):
        """
        Change the name of an item in the cart.
        """
        if old_name not in self.cart:
            print("Item not found.")
        else:
            self.cart[new_name] = self.cart.pop(old_name)
            print("Item name updated.")

    def update_item_quantity(self, item_name, new_quantity):
        """
        Update quantity for a specific item.
        """
        if item_name not in self.cart:
            print("Item not found.")
        else:
            self.cart[item_name][0] = new_quantity
            print("Quantity updated.")

    def update_item_price(self, item_name, new_price):
        """
        Update price for a specific item.
        """
        if item_name not in self.cart:
            print("Item not found.")
        else:
            self.cart[item_name][1] = new_price
            print("Price updated.")

    def delete_item(self, item_name):
        """
        Remove a specific item from the cart.
        """
        if item_name not in self.cart:
            print("Item not found.")
        else:
            del self.cart[item_name]
            print("Item removed.")

    def reset_cart(self):
        """
        Clear all items in the cart.
        """
        self.cart.clear()
        print("All items have been removed.")

    def check_order(self):
        """
        Display all items in the cart in a formatted table.
        """
        if not self.cart:
            print("Your cart is empty.")
            return

        table = []
        for idx, (name, values) in enumerate(self.cart.items(), start=1):
            quantity = values[0]
            price = values[1]
            total = quantity * price
            table.append([idx, name, quantity, price, total])

        headers = ["No", "Item Name", "Quantity", "Price/Item", "Total Price"]
        print(tabulate(table, headers=headers, tablefmt="grid"))

    def total_price(self):
        """
        Calculate and print the total cost after discount.

        Discounts:
        - > 500,000 → 10%
        - > 300,000 → 8%
        - > 200,000 → 5%
        """
        total = sum(qty * price for qty, price in self.cart.values())

        if total > 500000:
            discount = 0.10
        elif total > 300000:
            discount = 0.08
        elif total > 200000:
            discount = 0.05
        else:
            discount = 0.0

        final_amount = total - (total * discount)

        # ✅ NEW OUTPUT MESSAGE
        print(f"\nThe total transaction amount to be paid is: Rp {final_amount:,.0f}")
