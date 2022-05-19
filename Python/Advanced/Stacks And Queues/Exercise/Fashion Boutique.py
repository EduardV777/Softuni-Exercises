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

def HangClothes(stack, racksUsed, rackCap):
    sumRackUsage=0
    while stack.count():
        val=stack.peek()
        if val+sumRackUsage>rackCap:
            racksUsed+=1; sumRackUsage=0
            sumRackUsage+=val
        else:
            sumRackUsage += val
        stack.pop()
    return racksUsed


clothesDelivery=input(); rackCap=int(input())
racks=1
clothes=Stack()
clothesDelivery=clothesDelivery.split(" "); clothesDelivery=[int(e) for e in clothesDelivery]

for k in clothesDelivery:
    clothes.push(k)

print(HangClothes(clothes, racks, rackCap))