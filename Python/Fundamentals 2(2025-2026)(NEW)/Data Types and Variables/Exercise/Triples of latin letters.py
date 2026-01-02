n = int(input())

ind = 97

for k in range(ind, ind + n):
    for j in range(ind, ind + n):
        for c in range(ind, ind + n):
            print(chr(k) + chr(j) + chr(c))