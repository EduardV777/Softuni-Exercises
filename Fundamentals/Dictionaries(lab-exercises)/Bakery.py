string=input()
k=0; i=0
keys=[]; values=[]
while k<len(string):
    val=""
    if string[k]!=" ":
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
            values.append(int(val))
            i-=1
    else:
        k+=1
stocks=dict(zip(keys,values))
print(stocks)
