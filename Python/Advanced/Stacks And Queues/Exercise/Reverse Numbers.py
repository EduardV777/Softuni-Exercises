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

def ShowStack(stack):
    output = ""
    while stack.count():
        output+=stack.peek()
        stack.pop()
        if stack.count()!=0:
            output+=" "
    print(output)

integers=input()
integers=integers.split(" ")
numStack=Stack()

for k in integers:
    numStack.push(k)

ShowStack(numStack)