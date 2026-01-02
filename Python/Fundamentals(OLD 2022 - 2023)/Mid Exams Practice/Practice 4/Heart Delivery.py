evenNums=input()
evenNums=evenNums.split("@"); evenNums=[int(e) for e in evenNums]
k=0; failed=0; success=True
while True:
    command=input()
    if command!="Love!":
        if "Jump" in command:
            command=command.split(" ")
            length=int(command[1])
            k+=length
            if k>len(evenNums)-1:
                k=0
            if evenNums[k]==0:
                print(f"Place {k} already had Valentine's day.")
                continue
            if evenNums[k]==0:
                print(f"Place {k} has Valentine's day.")
            else:
                evenNums[k]-=2
                if evenNums[k]<=0:
                    evenNums[k]=0
                    print(f"Place {k} has Valentine's day.")
    else:
        print(f"Cupid's last position was {k}.")
        for k in range(0,len(evenNums)):
            if success==True and evenNums[k]==0:
                continue
            elif success==False and evenNums[k]==0:
                continue
            else:
                success=False
                failed+=1
        if success==True:
            print("Mission was successful.")
            break
        else:
            print(f"Cupid has failed {failed} places.")
            break
