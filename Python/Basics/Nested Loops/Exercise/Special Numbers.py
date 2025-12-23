#for a number to be special it needs n to be divisible by each of it's digits
n = int(input())

printFormat = ""

for k in range(1111, 10000):
    special = True
    c = str(k)

    for j in range(0,len(c)):
        if int(c[j]) == 0 or n % int(c[j]) != 0:
            special = False
            break

    if special:
        printFormat += f"{k} "

print(printFormat)
