def tea_calculator(piece, price):
    total = piece * price
    return total


piece = int(input("Enter the number of tea: "))
price = int(input("Enter the unit price: "))
result = tea_calculator(piece, price)
print("Total price: ",result)