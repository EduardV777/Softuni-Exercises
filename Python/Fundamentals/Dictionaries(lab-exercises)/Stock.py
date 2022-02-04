string=input()
k=0; i=0
keys=[]; values=[]; productsToLookFor=[]

while k<len(string):
    if string[k]!=" ":
        val=""
        for j in range(k,len(string)):
            if string[j]!=" ":
                val+=string[j]
                k+=1
            else:
                break
        if i==0:
            keys.append(val)
            i+=1
        else:
            values.append(val)
            i-=1
    else:
        k+=1

stocks=dict(zip(keys,values))
searchingFor=input()
k=0

while k<len(searchingFor):
    if searchingFor[k]!=" ":
        val=""
        for j in range(k,len(searchingFor)):
            if searchingFor[j]!=" ":
                val+=searchingFor[j]
                k+=1
            else:
                break
        productsToLookFor.append(val)
    else:
        k+=1

for k in range(0,len(productsToLookFor)):
    if stocks.get(productsToLookFor[k])!=None:
        msg=stocks.get(productsToLookFor[k])
        print(f"We have {msg} of {productsToLookFor[k]} left")
    else:
        print(f"Sorry, we don't have {productsToLookFor[k]}")
