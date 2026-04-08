def order_calculator(piece, price):
    total = piece * price
    return total


piece = int(input("Enter the number of coffees: "))
price = int(input("Enter the unit price: "))
result = order_calculator(piece, price)

print("Total price:", result)