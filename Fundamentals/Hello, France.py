collectionOfItems=input(); budget=float(input())
collectionOfItems=collectionOfItems.split("|"); itemsBought=[]
profits=0
for j in range(0,len(collectionOfItems)):
    collectionOfItems[j]=collectionOfItems[j].split("->")
    collectionOfItems[j][1]=float(collectionOfItems[j][1])

for k in range(0,len(collectionOfItems)):
    if collectionOfItems[k][0]=="Clothes":
        if collectionOfItems[k][1]<=50.00:
            if budget>=collectionOfItems[k][1]:
                budget-=collectionOfItems[k][1]
                itemsBought.append([collectionOfItems[k][0],collectionOfItems[k][1]])
        else:
            continue
    elif collectionOfItems[k][0]=="Shoes":
        if collectionOfItems[k][1]<=35.00:
            if budget>=collectionOfItems[k][1]:
                budget-=collectionOfItems[k][1]
                itemsBought.append([collectionOfItems[k][0],collectionOfItems[k][1]])
        else:
            continue
    elif collectionOfItems[k][0]=="Accesories":
        if collectionOfItems[k][1]<=20.50:
            if budget>=collectionOfItems[k][1]:
                budget-=collectionOfItems[k][1]
                itemsBought.append([collectionOfItems[k][0],collectionOfItems[k][1]])
        else:
            continue
output=""
for j in range(0,len(itemsBought)):
    profits += itemsBought[j][1] * 0.40
    itemsBought[j][1]+=(itemsBought[j][1])*0.40
    budget+=itemsBought[j][1]
    if j!=len(itemsBought)-1:
        output+=f"{round(itemsBought[j][1],2)} "
    else:
        output += f"{round(itemsBought[j][1], 2)}"
print(output)
print(f"Profit: {profits:.2f}")
if budget>=150:
    print("Hello, France!")
else:
    print("Not enough money.")
