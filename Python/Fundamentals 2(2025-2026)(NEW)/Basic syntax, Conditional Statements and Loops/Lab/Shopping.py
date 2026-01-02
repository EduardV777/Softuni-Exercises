budget = int(input())

while True:
    price = input()

    if price != "End":
        if price.isdigit():
            price = int(price)

            if price <= budget:
                budget -= price

            else:
                print("You went in overdraft!")
                break
    else:
        print("You bought everything needed.")
        break
