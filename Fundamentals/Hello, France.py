items=input(); budget=float(input())
itemsList=[]; profit=0; prices=""; moneySpentOnItems=0
k=0
while k<len(items):
    type=""; price=""
    if items[k] != "-" and items[k] != ">" and items[k] != "|":
        if items[k].isalpha()==True:
            for j in range(k,len(items)):
                if items[j]!="-" and items[j]!=">" and items[j]!="|":
                    type+=items[j]
                    k+=1
                else:
                    k+=1
                    break
            itemsList.append([type])
        elif items[k].isdigit()==True or items[k]==".":
            for j in range(k,len(items)):
                if items[j]!="-" and items[j]!=">" and items[j]!="|":
                    price+=items[j]
                    k+=1
                else:
                    k+=1
                    break
            itemsList[len(itemsList)-1].append(price)
    else:
        k+=1
for k in range(0,len(itemsList)):
    for j in range(0,1):
        if itemsList[k][j]=="Clothes":
            if float(itemsList[k][j+1])<=50.00:
                if budget>=float(itemsList[k][j+1]):
                    budget-=float(itemsList[k][j+1])
                    moneySpentOnItems += float(itemsList[k][j + 1])
                    prices += str(round(float(itemsList[k][j + 1]) + (float(itemsList[k][j + 1]) * 0.4),2))+" "
                    profit+=float(itemsList[k][j+1])+(float(itemsList[k][j+1])*0.4)
        elif itemsList[k][j]=="Shoes":
            if float(itemsList[k][j + 1]) <= 35.00:
                if budget>=float(itemsList[k][j+1]):
                    budget-=float(itemsList[k][j+1])
                    moneySpentOnItems += float(itemsList[k][j + 1])
                    prices += str(round(float(itemsList[k][j + 1]) + (float(itemsList[k][j + 1]) * 0.4),2))+" "
                    profit += float(itemsList[k][j + 1]) + (float(itemsList[k][j + 1]) * 0.4)
        elif itemsList[k][j]=="Accessories":
            if float(itemsList[k][j + 1]) <= 20.50:
                if budget>=float(itemsList[k][j+1]):
                    budget -= float(itemsList[k][j + 1])
                    moneySpentOnItems+=float(itemsList[k][j + 1])
                    prices += str(round(float(itemsList[k][j + 1]) + (float(itemsList[k][j + 1]) * 0.4),2))+" "
                    profit+=round(float(itemsList[k][j + 1]) + (float(itemsList[k][j + 1]) * 0.4),2)
budget+=profit
profit-=moneySpentOnItems
print(f"{prices}\nProfit: {profit:.2f}")
if budget>=150:
    print("Hello, France!")
else:
    print("Not enough money.")
