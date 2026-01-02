import re
furniture=[]
totalCost=0
checkValidityOfInput=re.compile(r"^>>[A-Za-z]+<<[0-9]+[.]?[0-9]+![0-9]+$")
checkFurniture=re.compile(r"\b([A-Za-z]+)\b")
checkPrice=re.compile(r"\b(<<)([0-9]+[.]?[0-9]+)(!)\b")
checkQuantity=re.compile(r"\b(!)([0-9]+)\b")
while True:
    command=input()
    if command!="Purchase":
        name=""; price=0; qty=0
        valid=checkValidityOfInput.search(command)
        if valid!=None:
            name=checkFurniture.findall(command)
            price=checkPrice.findall(command); price=float(price[0][1])
            qty=checkQuantity.findall(command); qty=int(qty[0][1])
            furniture.append(name[0])
            totalCost+=price*qty
    else:
        print("Bought furniture:")
        print('\n'.join(furniture))
        print(f"Total money spend: {totalCost:.2f}")
        break
