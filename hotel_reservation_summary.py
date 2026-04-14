def reservation_summary(name, day, pay):
    return day * pay


def is_breakfast_included(breakfast_included):
    if breakfast_included == "y":
        extra = reservation_summary(name, day, pay) + 500
        return extra

    elif breakfast_included == "n":
        return reservation_summary(name, day, pay)

    else:
        return "Invalid character entry! "


name = input("Enter your name: ")

day = int(input("Please enter how many days you wish to stay: "))
if day <= 0:
    print("Sorry, incorrect entry!")

pay = int(input("How much would you like to pay: "))

breakfast_included = input("Do you have a breakfast? (y/n): ")
if breakfast_included == "y":
    reservation_pay = reservation_summary(name, day, pay)
    breakfast = is_breakfast_included(breakfast_included)
    print(f"Merhaba, {name} {day} gecelik konaklama tutarınız {breakfast} TL'dir.")

else:
    reservation_pay = reservation_summary(name, day, pay)
    print(f"Merhaba, {name} {day} gecelik konaklama tutarınız {reservation_pay} TL'dir.")
