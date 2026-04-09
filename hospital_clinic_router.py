def determine_polyclinic(age):
    if 0 <= age <= 17:
        return "Children's Polyclinic"

    elif age >= 18:
        return "Adult Polyclinic"

    else:
        return "Invalid Age"


def priority_order(age):
    if age >= 65:
        return "Priority Patient"

    else:
        return "Patient Without Priority Status"


age = int(input("Enter your age: "))
result = determine_polyclinic(age)
priority = priority_order(age)
print(result)
print(priority)
