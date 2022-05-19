a=set([1,2,3,4])
b=set([5,6,7,8])
print("Set 'A'")
print(a)
print("Set 'B'")
print(b)

print("\n")

c=a.union(b)
print("Set 'C'(Result of union operator performed on 'A' and 'B')")
print(c)

d=set([3,3,7,9,10])
e=set([6,7,8,3,3])

print("\nSet 'D'")
print(d)
print("Set 'E'")
print(e)

f=d.intersection(e)

print("Set 'F'(Result of intersection operator performed on 'D' and 'E')")
print(f)

print('\n\nPassing elements into a set from a list using set comprehension')

l=[34,54,76,101,23]
print("List 'L'")
print(l)
s=set([]); s={e for e in l}
print("Set 'S'")
print(s)