n = int(input())
a = 1
b = 1
c = 1
printFormat = ""
while a <= n:
    while b <= a:
        printFormat += f"{c} "
        b += 1
        c += 1
        if c > n:
            a = n + 1
            break
    a += 1
    b = 1
    printFormat += "\n"

print(printFormat)