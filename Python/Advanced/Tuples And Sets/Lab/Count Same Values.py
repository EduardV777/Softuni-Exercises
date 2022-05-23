numbers=input()
numbers=numbers.split(" ")
numbers=[float(e) for e in numbers]
numbersTup=tuple(e for e in numbers)
outputOrder=[]

for k in range(0,len(numbers)):
    if not numbers[k] in outputOrder:
        outputOrder.append(numbers[k])

for k in outputOrder:
    print(f"{k} - {numbersTup.count(k)} times")