lengths=input()
lengths=lengths.split(" "); lengths=[int(integer) for integer in lengths]

n=lengths[0]; m=lengths[1]

elements=set([])
elements2=set([])

while n:
    e=input()
    elements.add(e)
    n-=1

while m:
    e=input()
    elements2.add(e)
    m-=1

interSet=elements.intersection(elements2)

while interSet:
    print(interSet.pop())