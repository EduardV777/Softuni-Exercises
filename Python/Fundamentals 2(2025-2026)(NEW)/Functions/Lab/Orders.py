def order(product = input(), quantity = int(input())):

    price = 0

    #prices
    # coffee = 1.50
    # water = 1.00
    # coke = 1.40
    # snacks = 2.00

    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00

    return f"{price * quantity:.2f}"

print(order())