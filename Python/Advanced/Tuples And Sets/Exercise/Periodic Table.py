n=int(input())
chemicalsSet=set([])
while n:
    chemicals=input(); chemicals=chemicals.split(" ")
    for k in chemicals:
        chemicalsSet.add(k)
    n-=1

while len(chemicalsSet):
    print(chemicalsSet.pop())