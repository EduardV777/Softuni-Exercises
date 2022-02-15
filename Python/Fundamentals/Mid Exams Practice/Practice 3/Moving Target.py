targets=input()
targets=targets.split(" "); targets=[int(num) for num in targets]
while True:
    command=input()
    if command!="End":
        if "Shoot" in command:
            command=command.split(" ")
            ind=int(command[1]); power=int(command[2])
            if 0<=ind<len(targets):
                targets[ind]-=power
                if targets[ind]<=0:
                    targets.pop(ind)
        elif "Add" in command:
            command=command.split(" ")
            ind=int(command[1]); value=int(command[2])
            if 0<=ind<len(targets):
                targets.insert(ind,value)
            else:
                print("Invalid placement!")
                continue
        elif "Strike" in command:
            command=command.split(" ")
            ind=int(command[1]); radius=int(command[2])
            initInd=ind; k=0
            if ind-radius>=0 and ind+radius<len(targets):
                targets[ind]="Striked"
                while k<radius:
                    ind+=1; k+=1
                    targets[ind]="Striked"
                ind=initInd; k=0
                while k<radius:
                    ind-=1; k+=1
                    targets[ind]="Striked"
                k=0
                while k<len(targets):
                    if targets[k]=="Striked":
                        del targets[k]
                    else:
                        k+=1
            else:
                print("Strike missed!")
                continue
    else:
        targets=[str(num) for num in targets]
        print(f"{'|'.join(targets)}")
        break
