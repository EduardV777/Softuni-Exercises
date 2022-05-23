nNames=int(input())
uniqueNames=set({})
while nNames!=0:
    name=input()
    uniqueNames.add(name)
    nNames-=1

while len(uniqueNames)!=0:
    print(uniqueNames.pop())