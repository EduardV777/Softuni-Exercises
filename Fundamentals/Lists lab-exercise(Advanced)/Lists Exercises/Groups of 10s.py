from math import ceil
numbers=input()
numbers=numbers.split(", ")
numbers=[int(e) for e in numbers]
groupVal=10
boundary=ceil(max(numbers)/10)
groups=[]
while len(numbers)!=0:
    groups.append(list(filter(lambda x: groupVal-10<x<=groupVal,numbers)))
    j=0
    while j<len(numbers):
        if groupVal-10<numbers[j]<=groupVal:
            del numbers[j]
        else:
            j+=1
    print(f"Group of {groupVal}'s: {groups[len(groups)-1]}")
    groupVal+=10
