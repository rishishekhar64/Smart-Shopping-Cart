items = {
    "bread": 40,
    "milk": 30,
    "coffee": 120,
    "eggs": 60,
    "rice": 80
}

def show_menu():
    print("\nAvailable items:")
    for item, price in items.items():
        print(f"{item} - ₹{price}")

def calculate_bill(item, quantity):
    return items[item] * quantity

def shopping_main():
    total = 0
    print("Welcome to Python Mart!")

    while True:
        show_menu()
        item = input("Enter item to buy (or 'done' to finish): ").lower()

        if item == "done":
            break

        if item not in items:
            print("Item not available!")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be positive!")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue

        cost = calculate_bill(item, quantity)
        total += cost
        print(f"Added {item} × {quantity} = ₹{cost}")

    print(f"\nSubtotal = ₹{total}")

    if total > 500:
        discount = total * 0.10
        total -= discount
        print(f"Discount (10%) = ₹{discount:.2f}")

    print(f"Total Payable = ₹{total:.2f}")
    print("Thank you for shopping!")

# Run the program
shopping_main()
