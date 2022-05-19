from collections import deque

qtyFood=int(input()); integers=input()
integers=integers.split(" "); integers=[int(e) for e in integers]
maxOrder=max(integers)
orders=deque([])


def fillQueue(queue):
    val = ""
    for k in range(0,len(integers)):
        queue.append(integers[k])

fillQueue(orders)
servedAll=True; remainingOrders=""
while orders:
    currOrder = orders.popleft()
    if servedAll==False:
        remainingOrders+=str(currOrder)+" "
    if qtyFood>=currOrder:
        qtyFood-=currOrder
    else:
        if servedAll==True:
            orders.appendleft(currOrder)
            servedAll=False

print(maxOrder)
if servedAll==True:
    print("Orders complete")
else:
    print("Orders left: "+remainingOrders)

