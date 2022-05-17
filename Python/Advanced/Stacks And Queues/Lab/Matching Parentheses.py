from collections import deque

expression=input()

expQueue=deque([])

def FindBracketedExps(queue,mathExp,ind=0):
    openBrackets = 0; bracketedExp = ""
    for k in range(ind,len(expression)):
        if expression[k]=="(":
            openBrackets+=1
            if openBrackets>1:
                FindBracketedExps(queue,expression, k)
        if expression[k]==")":
            openBrackets-=1
            if openBrackets==0:
                bracketedExp+=")"
        if openBrackets>0:
            bracketedExp+=expression[k]
        elif bracketedExp!="" and openBrackets==0:
            queue.append(bracketedExp)
            bracketedExp=""
            if ind!=0:
                break

FindBracketedExps(expQueue,expression)
output=""
while expQueue:
    output+=expQueue.popleft()
    if len(expQueue):
        output+="\n"
print(output)