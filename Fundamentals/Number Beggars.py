strInt=input(); beggars=int(input())
integers=[]; beggarsLoot=[]
#create beggar's loot stats
for k in range(0,beggars):
    beggarsLoot.append(0)
k=0; num=0
#fill list
while k<len(strInt):
    num=""
    if strInt[k].isdigit():
        for j in range(k,len(strInt)):
            if strInt[j]!=",":
                k+=1
                num+=strInt[j]
            else:
                break
        integers.append(num)
    elif strInt[k]=="," or strInt[k]==" ":
        k+=1
        continue
beggar=0
for k in range(0,len(integers)):
    for j in range(beggar,beggars):
        beggarsLoot[j]+=int(integers[k])
        if beggar==beggars-1:
            beggar=0
        else:
            beggar += 1
        break
print(beggarsLoot)
