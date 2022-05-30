from collections import deque

class Stack():
    def __init__(self,label=""):
        self.label=label
    stack=[]

    def peek(self):
        return self.stack[-1]
    def push(self, e):
        self.stack.append(e)
    def count(self):
        return len(self.stack)
    def pop(self):
        self.stack.pop()

    def __repr__(self):
        return f"stack({self.label})["+', '.join(self.stack)+"]"

chocs=input(); milkCups=input()
chocs=chocs.split(", "); milkCups=milkCups.split(", ")

chocolateStack=Stack()
milkCupsQueue=deque([])
milkshakesPrepared=0


for k in chocs:
    chocolateStack.push(int(k))

for j in milkCups:
    milkCupsQueue.append(int(j))



while chocolateStack.count()!=0:
    if milkshakesPrepared==5 or len(milkCupsQueue)==0:
        break
    currChocVal=chocolateStack.peek()
    chocolateStack.pop()
    currMilkVal=milkCupsQueue.popleft()
    if not currChocVal<=0 and not currMilkVal<=0:
        if currChocVal==currMilkVal:
            milkshakesPrepared+=1
        else:
            milkCupsQueue.append(currMilkVal)
            currChocVal-=5
            chocolateStack.push(currChocVal)
    else:
        if not currChocVal<=0:
            chocolateStack.push(currChocVal)
        if not currMilkVal<=0:
            milkCupsQueue.appendleft(currMilkVal)


if milkshakesPrepared==5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolateStack.count()!=0:
    output="Chocolate: "; vals=[]
    while chocolateStack.count()!=0:
        vals.append(str(chocolateStack.peek()))
        chocolateStack.pop()
    for k in range(len(vals)-1,-1,-1):
        output+=vals[k]
        if k!=0:
            output+=", "
    print(output)
else:
    print("Chocolate: empty")


if len(milkCupsQueue)!=0:
    output="Milk: "
    while len(milkCupsQueue)!=0:
        output+=str(milkCupsQueue.popleft())
        if len(milkCupsQueue)!=0:
            output+=", "
    print(output)
else:
    print("Milk: empty")
