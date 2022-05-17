import random

class Stack():
    stack = []
    def __init__(self, length):
        output=""
        for k in range(0,length):
            val=round(1+random.random()*10)
            output+=str(val)
            if(k!=length-1):
                output+=", "
            self.stack.append(val)
        print(f"Stack created with {length} random elements")
        print("Stack contents: "+output+"\n")
    def push(self, val):
        self.stack.append(val)
    def peek(self):
        print(self.stack[-1])
    def count(self):
        print(f"Stack length: {len(self.stack)}")
    def pop(self):
        self.stack.pop()
stack1=Stack(10)

stack1.peek()
stack1.pop()
stack1.peek()
stack1.count()
stack1.push(900)
stack1.peek()
stack1.count()