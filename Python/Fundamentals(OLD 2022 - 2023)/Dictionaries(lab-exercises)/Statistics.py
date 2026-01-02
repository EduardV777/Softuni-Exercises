products={}
while True:
    command=input()
    if command!="statistics":
        k=0; i=0
        product=""; qty=0
        while k<len(command):
            if command[k]!=":":
                val=""
                for j in range(k,len(command)):
                    if command[j]!=":":
                        val+=command[j]
                        k+=1
                    else:
                        break
                if i==0:
                    product=val
                    i+=1
                else:
                    qty+=int(val)
            else:
                k+=1
        if products.get(product)!=None:
            currentQty=products[product]
            currentQty+=qty
            products[product]=currentQty
        else:
            products[product]=qty
    else:
        countProducts=0; countProductsQty=0
        print("Products in stock:")
        for k in products:
            print(f"- {k}: {products[k]}")
            countProducts+=1
            countProductsQty+=products[k]
        print(f"Total Products: {countProducts}\nTotal Quantity: {countProductsQty}")
        break
