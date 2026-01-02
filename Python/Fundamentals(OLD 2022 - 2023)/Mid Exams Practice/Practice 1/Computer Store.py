partsPrices=[]
receipt=""
costWithoutTax=0; costWithTax=0; taxes=0
def addToPartsPricesList(inputHere):
    partsPrices.append(inputHere)

while True:
    userInput=input()
    if userInput.isdigit():
        userInput=float(userInput)
        if userInput<0:
            print("Invalid price!")
            continue
        addToPartsPricesList(userInput); costWithoutTax+=userInput
    else:
        if "." in userInput or "-" in userInput:
            floatValue=True
            #make sure it's not float price value/or negative value
            if "-" in userInput:
                print("Invalid price!")
                continue
            userInput=userInput.split(".")
            for k in range(0,len(userInput)):
                if not userInput[k].isdigit:
                    floatValue==False
                    break
            if floatValue==True:
                userInput=".".join(userInput); userInput = float(userInput)
                if userInput < 0:
                    print("Invalid price!")
                    continue
                addToPartsPricesList(userInput); costWithoutTax += userInput
                continue

        for k in range(0,len(partsPrices)):
            costWithTax+=partsPrices[k]+(partsPrices[k]*0.2)
            taxes+=(partsPrices[k]*0.2)
        if costWithTax==0:
            print("Invalid order!")
            break
        if userInput=="special":
            costWithTax-=(costWithTax*0.1)
        elif userInput=="regular":
            pass
        receipt=f"Congratulations you've just bought a new computer!\nPrice without taxes: {costWithoutTax:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {costWithTax:.2f}$"
        print(receipt)
        break
