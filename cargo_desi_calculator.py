def desi_calculator(width, length, height):
    if width <= 0 or length <= 0 or height <= 0:

        return "Invalid item"

    else:
        desi = float(width * length * height) / 3000

        return desi


def cargo_type_selection(width, length, height):
    desi = float(width * length * height) / 3000

    if 0 <= desi < 10:
        return "Small cargo"

    elif 10 <= desi <= 20:
        return "Medium cargo"

    elif desi > 20:
        return "Large cargo"


width = int(input("Enter width :"))
length = int(input("Enter length :"))
height = int(input("Enter height :"))

if width <= 0 or length <= 0 or height <= 0:
    print("Invalid item")

else:

    desi_cal = desi_calculator(width, length, height)
    print("Desi Calculator :", desi_cal)

    cargo_type = cargo_type_selection(width, length, height)
    print("Cargo Type :", cargo_type)
