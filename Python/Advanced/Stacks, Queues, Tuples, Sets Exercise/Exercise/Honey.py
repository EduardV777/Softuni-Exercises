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


workerBees=input(); nectar=input(); symbols=input()
workerBees=workerBees.split(" "); nectar=nectar.split(" "); symbols=symbols.split(" ")

workerBeesQueue=deque([])
symbolsQueue=deque([])
nectarStack=Stack('nectar')
totalHoney=0

for k in workerBees:
    workerBeesQueue.append(k)
for j in nectar:
    nectarStack.push(j)
for i in symbols:
    symbolsQueue.append(i)

while nectarStack.count()!=0:
    if len(workerBeesQueue)==0:
        break
    currNectar=nectarStack.peek()
    nectarStack.pop()
    currBeeVal=workerBeesQueue.popleft()

    if int(currNectar)>=int(currBeeVal):
        currSymbol=symbolsQueue.popleft()
        calcMadeHoney=abs(eval(currBeeVal+currSymbol+currNectar))
        totalHoney+=calcMadeHoney
    else:
        workerBeesQueue.appendleft(currBeeVal)

print(f"Total honey made: {totalHoney}")

k=0
while k<=1:
    output=""
    if k==0:
        if len(workerBeesQueue)!=0:
            output="Bees left: "
            while len(workerBeesQueue)!=0:
                output+=workerBeesQueue.popleft()
                if len(workerBeesQueue)!=0:
                    output+=", "
            print(output)
    if k==1:
        if nectarStack.count()!=0:
            output="Nectar left: "; vals=[]
            while nectarStack.count()!=0:
                vals.append(nectarStack.peek())
                nectarStack.pop()
            for i in range(len(vals)-1,-1,-1):
                output+=vals[i]
                if i!=0:
                    output += ", "
            print(output)
    k+=1