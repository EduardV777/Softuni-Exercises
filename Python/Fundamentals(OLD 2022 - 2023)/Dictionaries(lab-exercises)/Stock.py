productsAndQty=input(); productsToSearch=input()
productsAndQty=productsAndQty.split(" "); productsToSearch=productsToSearch.split(" ")
products=[e for e in productsAndQty if e.isdigit()==False]
quantities=[int(e) for e in productsAndQty if e.isdigit()==True]
storage=dict(zip(products,quantities))

for k in range(0,len(productsToSearch)):
    available=storage.get(productsToSearch[k], "no")
    if available=="no":
        print(f"Sorry, we don't have {productsToSearch[k]}")
    else:
        print(f"We have {available} of {productsToSearch[k]} left")
