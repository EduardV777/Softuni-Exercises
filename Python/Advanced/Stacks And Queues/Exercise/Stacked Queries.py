class Stack():
    stackVar=[]
    def peek(self):
        return self.stackVar[-1]
    def push(self, val):
        self.stackVar.append(val)
    def pop(self):
        self.stackVar.pop()
    def count(self):
        return len(self.stackVar)
    def __repr__(self):
        return "[STACK](["+', '.join(self.stackVar)+"])"

n=int(input())
numStack=Stack()

def ShowStack(stack):
    output = ""
    while stack.count():
        output+=str(stack.peek())
        stack.pop()
        if stack.count()!=0:
            output+=", "
    print(output)


while n!=0:
    query=input()
    if '1' in query:
        number=query.split(" ")
        number=int(number[1])
        numStack.push(number)
    elif '2' in query:
        if numStack.count()!=0:
            numStack.pop()
    elif '3' in query:
        if numStack.count()!=0:
            maxNum=max(numStack.stackVar)
            print(maxNum)
    elif '4' in query:
        if numStack.count() != 0:
            minNum = min(numStack.stackVar)
            print(minNum)
    n-=1
ShowStack(numStack)