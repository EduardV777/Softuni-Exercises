product=input(); quantity=int(input())
def orderProcess(prod="", qty=0):
    if prod=="coffee":
        price=1.50
    elif prod=="water":
        price=1.00
    elif prod=="coke":
        price=1.40
    elif prod=="snacks":
        price=2.00
    total=price*qty
    return total
print(f"{orderProcess(product,quantity):.2f}")
