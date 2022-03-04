products={}
while True:
    command=input()
    if command!="buy":
        command=command.split(" ")
        command[1]=float(command[1]); command[2]=int(command[2])
        doesItExist=products.get(command[0],"no")
        if doesItExist!="no":
            products[command[0]][0]=command[1]
            products[command[0]][1]+=command[2]
        else:
            products[command[0]]=[command[1],command[2]]
    else:
        for j in products:
            print(f"{j} -> {products[j][0]*products[j][1]:.2f}")
        break
