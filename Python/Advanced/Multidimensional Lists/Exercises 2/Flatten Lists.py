lists=input(); lists=lists.split("|")
k=0
matrix=[]

for k in range(0,len(lists)):
    lists[k] = lists[k].split(" ")
    j=0
    while j<len(lists[k]):
        if lists[k][j]=='' or lists[k][j]==' ':
            del lists[k][j]
        else:
            j+=1

print(' '.join([' '.join(lists[e]) for e in range(len(lists)-1,-1,-1)]))