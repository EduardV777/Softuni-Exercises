elements=input()
elements=elements.split(" ")
moves=0
while True:
    indexes=input()
    if indexes!="end":
        indexes=indexes.split(" ")
        for k in range(0,len(indexes)):
            if "-" in indexes[k]:
                indexes[k]=indexes[k].split("-")
                indexes[k]=int(indexes[k][1])*-1
            else:
                indexes[k]=int(indexes[k])
        moves+=1
        if indexes[0]==indexes[1] or (not 0<=indexes[0]<=len(elements)-1 or not 0<=indexes[1]<=len(elements)-1):
            #we have same indexes
            if len(elements)>0:
                mid=len(elements)//2
                matchingElements=f"-{moves}a"
                elements.insert(mid,matchingElements); elements.insert(mid,matchingElements)
                print("Invalid input! Adding additional elements to the board")
            else:
                moves-=1
                pass
        else:
            if elements[indexes[0]]==elements[indexes[1]]:
                #we have matching elements
                print(f"Congrats! You have found matching elements - {elements[indexes[0]]}!")
                if indexes[0]>indexes[1]:
                    del elements[indexes[0]]; del elements[indexes[1]]
                else:
                    del elements[indexes[1]]; del elements[indexes[0]]
            else:
                print("Try again!")
    else:
        if len(elements)==0:
            print(f"You have won in {moves} turns!")
        else:
            print(f"Sorry you lose :( \n{' '.join(elements)}")
        break
