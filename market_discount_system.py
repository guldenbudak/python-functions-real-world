def find_the_discount_rate(basket_total):
    if 0 <= basket_total <= 499:
        return 0.0

    elif 499 < basket_total <= 999:
        return 0.05

    elif 1000 <= basket_total <= 1999:
        return 0.10

    elif basket_total >= 2000:
        return 0.15


def discounted_amount_calculate(basket_total):
    if discount_to_be_applied == 0.0:
        discount = basket_total
        return discount

    elif discount_to_be_applied == 0.05:
        discount = basket_total - ((basket_total * 5) / 100)
        return discount

    elif discount_to_be_applied == 0.10:
        discount = basket_total - ((basket_total * 10) / 100)
        return discount

    elif discount_to_be_applied == 0.15:
        discount = basket_total - ((basket_total * 15) / 100)
        return discount


def coupon_code_calculator(coupon_code):
    if coupon_code == "y":
        extra = discounted_price - 50
        return "The coupon has been applied: ", extra

    elif coupon_code == "n":
        return "The coupon was not applied: ", discounted_price

    else:
        return "Invalid coupon code: "


coupon_code = input("Do you have a coupon code? (y/n): ")

basket_total = int(input("Enter your basket total: "))
if basket_total <= 0:
    print("Please enter a valid value ! ")

else:
    discount_to_be_applied = find_the_discount_rate(basket_total)
    print("Discount to be applied: ", discount_to_be_applied)

    discounted_price = discounted_amount_calculate(basket_total)
    print("Discounted price: ", discounted_price)

    coupon_extra = coupon_code_calculator(coupon_code)
    print("Coupon code: ", coupon_extra)
