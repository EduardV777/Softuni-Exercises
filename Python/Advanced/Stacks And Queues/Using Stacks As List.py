"""
Stacks methods:
-- peek()   / [-1]
-- pop()    / pop[-1]
-- push()   / append()
-- count() / len()
"""

def CreateStack(length=1):
    stack=[]
    for k in range(0,length):
        val=input(f"Value {k+1}: ")
        if(val>='0' and val<='9'):
            stack.append(int(val))
        else:
            stack.append(val)
    print("Stack created!")
    return stack

def ShowStack(stack):
    print(f"Stack length: {len(stack)}")
    output=""
    while stack:
        output+=str(stack[-1])
        stack.pop()
        if(len(stack)!=0):
            output+=", "
    return output

stack1=CreateStack(10)
print("\n")
print(ShowStack(stack1))