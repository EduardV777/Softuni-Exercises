from collections import deque

customerLine=deque([])

while True:
    customer=input("")
    if customer=="Paid":
        output=""
        while customerLine:
            output+=customerLine.pop()
            if len(customerLine)!=0:
                output+="\n"
        print(output)
    elif customer!="End":
        customerLine.appendleft(customer)
    elif customer=="End":
        print(f"{len(customerLine)} people remaining.")
        break