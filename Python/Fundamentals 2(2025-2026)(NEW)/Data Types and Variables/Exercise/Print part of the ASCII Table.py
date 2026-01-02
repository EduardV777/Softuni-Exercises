ind1 = int(input())
ind2 = int(input())


for k in range(ind1, ind2 + 1):
    if k != ind2:
        end = " "
    else:
        end = ""

    print(chr(k), end = end)