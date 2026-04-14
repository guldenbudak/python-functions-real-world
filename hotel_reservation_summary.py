def get_reservation_price(day, pay):
    return day * pay


def get_price_with_breakfast(day):
    extra = get_reservation_price(day, pay) + 500 * day
    return extra


name = input("Enter your name: ")
day = int(input("Please enter how many days you wish to stay: "))

if day <= 0:
    print("Sorry, incorrect entry!")

pay = int(input("How much would you like to pay: "))

breakfast_included = input("Do you have a breakfast? (y/n): ")

if breakfast_included == "y":
    total_price = get_price_with_breakfast(day)
    print(f"Merhaba, {name} {day} gecelik konaklama tutarınız {total_price} TL'dir.")
else:
    reservation_pay = get_reservation_price(day, pay)
    print(f"Merhaba, {name} {day} gecelik konaklama tutarınız {reservation_pay} TL'dir.")
