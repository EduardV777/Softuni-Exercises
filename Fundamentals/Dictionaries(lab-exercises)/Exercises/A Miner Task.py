i=0; resources={}
resource=""
while True:
    command=input()
    if command!="stop":
        resFound=False
        if i==0:
            for k in resources:
                if k==command:
                    resFound=True
                    break
            i+=1; resource=command
            if resFound==True:
                continue
            else:
                resources[command]=0
        elif i==1:
            resources[resource]+=int(command)
            i-=1
    else:
        output=""
        for k in resources:
            output+=f"{k} -> {resources[k]}\n"
        print(output)
        break
