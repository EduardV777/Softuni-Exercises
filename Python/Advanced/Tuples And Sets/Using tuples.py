numData=(1,2,3,2,2,3)

print(numData)

print("Length of tuple: "+str(len(numData)))
print("Elements amount: "+str(numData.count(2)))
print("Index of element 3: "+str(numData.index(3)))

#attempting to change a value in a tuple
try:
    numData[2]=4543
except TypeError:
    print("[ERROR]: Tried to change the value of a tuple sequence!")

print("Unpacking a tuple into variables...")
a1,a2,a3,a4,a5,a6=numData

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)