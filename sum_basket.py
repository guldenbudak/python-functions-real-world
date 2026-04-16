def sum_of_excess_basket_item(excess_product):
    total = 0
    for item in excess_product:
        total = total + item
    return "The total of products with a price above 500 :", total


def sum_of_basket_item(basket):
    sum = 0
    for item in basket:
        sum = sum + item

    if sum == 0:
        return "ERROR data collection :", 0

    else:
        return "The sum of the entered numbers :", sum


def get_basket_items():
    basket = []
    item_size = int(input("Enter item size: "))

    for item in range(item_size):
        item_price = int(input(f"Enter {item + 1} item price: "))

        basket.append(item_price)
    return basket


def items_priced_over_500(item_price):
    excess_product = []
    for product in item_price:
        if product >= 500:
            excess_product.append(product)
    return excess_product


def hesapla():
    basket = get_basket_items()
    excess_product = items_priced_over_500(basket)
    total = sum_of_excess_basket_item(excess_product)
    sum = sum_of_basket_item(basket)
    return sum, total


print(hesapla())
