ticket = 200


def calculate_ticket_price(age, time):
    if age < 12 and time < 11:
        discount = ticket - ((ticket * 50)) / 100
        extra_discount = discount - ((discount * 20)) / 100
        return extra_discount

    elif age < 12 and time > 11:
        discount = ticket - ((ticket * 50)) / 100
        return discount

    elif 59 >= age > 12 and time < 11:
        discount = ticket - ((ticket * 20)) / 100
        return discount

    elif 59 >= age > 12 and time > 11:
        return ticket

    elif age >= 60 and time < 11:
        discount = ticket - ((ticket * 30)) / 100
        extra_discount = discount - ((discount * 20)) / 100
        return extra_discount

    elif age >= 60 and time > 11:
        discount = ticket - ((ticket * 30)) / 100
        return discount


age = int(input("Enter your age : "))
time = int(input("Enter your time : "))

result = calculate_ticket_price(age, time)
print("Amount to be paid: ", result)
