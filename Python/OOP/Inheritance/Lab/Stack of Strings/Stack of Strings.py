class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[len(self.data)-1]

    def is_empty(self):

        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        copyStack = []
        output = "["

        while(self.is_empty() == False):
            val = self.pop()
            copyStack.append(val)
            output += val

            if self.is_empty() == False:
                output += ", "

        output += "]"
        self.data = copyStack
        del copyStack
        return output



#Test code

"""
newStack = Stack()

newStack.push('pizza')
newStack.push('dog')
newStack.push('tree')
print(newStack.top())
print(newStack.pop())
print(newStack)
print(newStack.is_empty())
print(newStack.pop())
print(newStack.pop())
print(newStack.is_empty())
"""