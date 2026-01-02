n = int(input())

pos = []
neg = []

sumNeg = 0

while n:
    num = int(input())

    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

    n -= 1

for k in neg:
    sumNeg += k

print(f"{pos}\n{neg}\nCount of positives: {len(pos)}\nSum of negatives: {sumNeg}")