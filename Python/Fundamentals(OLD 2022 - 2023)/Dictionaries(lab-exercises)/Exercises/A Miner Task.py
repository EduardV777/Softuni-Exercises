resourceStorage=dict()
k=1; ProdName=""
while True:
    command=input()
    if command!="stop":
        if k%2==0:
                resourceStorage[prodName]+=int(command)
                k+=1
        else:
            prodExists = resourceStorage.get(command, "no")
            prodName=command
            if prodExists=="no":
                resourceStorage[command]=0
            k+=1
    else:
        break

for j in resourceStorage:
    print(f"{j} -> {resourceStorage[j]}")
