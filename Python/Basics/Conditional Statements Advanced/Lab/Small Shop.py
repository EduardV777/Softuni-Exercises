product = input()
city = input()
qty = float(input())

coffeePrice = None
waterPrice = None
beerPrice = None
sweetsPrice = None
peanutsPrice = None

if city == "Sofia":
    coffeePrice = 0.50
    waterPrice = 0.80
    beerPrice = 1.20
    sweetsPrice = 1.45
    peanutsPrice = 1.60

    if product == "coffee":
        print(coffeePrice * qty)
    elif product == "water":
        print(waterPrice * qty)
    elif product == "beer":
        print(beerPrice * qty)
    elif product == "sweets":
        print(sweetsPrice * qty)
    elif product == "peanuts":
        print(peanutsPrice * qty)

elif city == "Plovdiv":
    coffeePrice = 0.40
    waterPrice = 0.70
    beerPrice = 1.15
    sweetsPrice = 1.30
    peanutsPrice = 1.50

    if product == "coffee":
        print(coffeePrice * qty)
    elif product == "water":
        print(waterPrice * qty)
    elif product == "beer":
        print(beerPrice * qty)
    elif product == "sweets":
        print(sweetsPrice * qty)
    elif product == "peanuts":
        print(peanutsPrice * qty)

elif city == "Varna":
    coffeePrice = 0.45
    waterPrice = 0.70
    beerPrice = 1.10
    sweetsPrice = 1.35
    peanutsPrice = 1.55

    if product == "coffee":
        print(coffeePrice * qty)
    elif product == "water":
        print(waterPrice * qty)
    elif product == "beer":
        print(beerPrice * qty)
    elif product == "sweets":
        print(sweetsPrice * qty)
    elif product == "peanuts":
        print(peanutsPrice * qty)