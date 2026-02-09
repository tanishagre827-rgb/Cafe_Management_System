# Define Menu for Restaurant
menu = {
    'Pizza': 100,
    'Pasta': 120,
    'Burger': 120,
    'Coffee': 70,
    'Momos': 80
}

# Greeting Customer
print("Welcome to Cafe Delight")
print("Pizza: Rs100\nPasta: Rs120\nBurger: Rs120\nCoffee: Rs70\nMomos: Rs80")

order_total = 0  # initialize total bill

# First Order
item_1 = input("Enter the name of the item you want to order: ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available!")

# Another Order
another_order = input("Do you want to add another item? (Yes/No): ").title()

if another_order == "Yes":
    item_2 = input("Enter the name of the item: ").title()

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

# Final Bill
print("\nTotal Amount to Pay: Rs", order_total)
print("Thank you for visiting Cafe Delight 😊")
