prices = [[2.50,1.20,0.85,1.45,2.70,5.50,3.85], [2.70,1.25,0.90,1.60,3.00,5.60,4.20]]

cost = 0

product = input()
day = input()
qty = float(input())
error = False

if day in "Monday Tuesday Wednesday Thursday Friday":
    if product == "banana":
        cost = qty * prices[0][0]
    elif product == "apple":
        cost = qty * prices[0][1]
    elif product == "orange":
        cost = qty * prices[0][2]
    elif product == "grapefruit":
        cost = qty * prices[0][3]
    elif product == "kiwi":
        cost = qty * prices[0][4]
    elif product == "pineapple":
        cost = qty * prices[0][5]
    elif product == "grapes":
        cost = qty * prices[0][6]
    else:
        print("error")
        error = True

elif day in "Saturday Sunday":
    if product == "banana":
        cost = qty * prices[1][0]
    elif product == "apple":
        cost = qty * prices[1][1]
    elif product == "orange":
        cost = qty * prices[1][2]
    elif product == "grapefruit":
        cost = qty * prices[1][3]
    elif product == "kiwi":
        cost = qty * prices[1][4]
    elif product == "pineapple":
        cost = qty * prices[1][5]
    elif product == "grapes":
        cost = qty * prices[1][6]

else:
    print("error")
    error = True

if not error:
    print(f"{cost:.2f}")