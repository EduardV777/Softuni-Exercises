collection=input(); budget=int(input())
collection=collection.split("|")
boughtItems=[]; initialBudget=budget
for k in range(0,len(collection)):
    currItem=collection[k].split("->")
    boughtSomething = False
    if currItem[0]=="Clothes":
        if float(currItem[1])<=50.00:
            boughtSomething = True
    elif currItem[0]=="Shoes":
        if float(currItem[1])<=35.00:
            boughtSomething = True
    elif currItem[0]=="Accessories":
        if float(currItem[1])<=20.50:
            boughtSomething = True
    if boughtSomething==True and budget>=float(currItem[1]):
        boughtItems.append(float(currItem[1]) + (float(currItem[1]) * 0.4))
        budget-=float(currItem[1])
printNewPrices=""
for k in range(0,len(boughtItems)):
    printNewPrices+=f"{boughtItems[k]:.2f}"
    if k!=len(boughtItems)-1:
        printNewPrices+=" "
    budget+=boughtItems[k]
print(f"{printNewPrices}\nProfit: {budget-initialBudget:.2f}")
if budget>=150:
    print("Hello, France!")
else:
    print("Not enough money.")
