def rent_a_car_fee(day,wages,category):
    total = day * wages
    if day >= 7:
        discount = total - ((total * 10) / 100)

        if category == 1:
            extra = discount - ((discount * 5) / 100)
            return extra

        else:
            return discount

    else:
        if category == 1:
            discount = total - ((total * 5) / 100)
            return discount

        else:
            return total



day = int(input("Enter the day: "))
wages = int(input("Enter the number of wages: "))
category =int(input("1-) Premium\n2-) Standart\nEnter the category of the rental: "))
result = rent_a_car_fee(day,wages,category)
print("Total price",result)