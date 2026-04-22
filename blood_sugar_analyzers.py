def lab_result_router(users):
    for item in users:
        result = ""
        if item < 70:
            print(f"{item} low")
            result = "low"

        elif 70 < item and item < 100:
            print(f"{item} normal")
            result = "normal"


        elif 100 <= item or item <= 125:
            print(f"{item} prediabetes")
            result = "prediabetes"


        elif item >= 126:
            print(f"{item} high")
            result = "high"

        else:
            print(f"{item} invalid result !!!")

    outcome_based_consultation(result)


def get_user_input():
    users = []
    item_size = int(input("Enter item size: "))

    for item in range(item_size):
        result = int(input(f"Enter {item + 1} conclusion: "))
        users.append(result)
    return users


def outcome_based_consultation(item):
    if item == "prediabetes":
        print("Prediabetes — It is recommended that you consult a doctor. ")

    else:
        print("Please continue your checks.")


get_user = get_user_input()
lab_result_router(users=get_user)