n = int(input())
word = input()

col = []
fil = []

while n:
    txt = input()
    col.append(txt)

    n -= 1

for k in col:
    if word in k:
        fil.append(k)


print(col)
print(fil)