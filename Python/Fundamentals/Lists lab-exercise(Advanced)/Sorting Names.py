names=input()
names=names.split(", ")
names=sorted(names,key=lambda x: (-len(x),x))
print(names)
