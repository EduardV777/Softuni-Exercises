from collections import deque

kidNames=input(); nToss=int(input())

kids=deque(kidNames.split(" "))

toss=0
while len(kids)>1:
    toss+=1
    kid=kids.popleft()
    if toss!=nToss:
        kids.append(kid)
    else:
        print(f"Removed {kid}")
        toss=0

print(f"Last is {kids.popleft()}")