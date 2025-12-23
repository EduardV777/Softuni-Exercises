#the sum of the digits in odd and even positions of the numbers should be equal
n1 = int(input())
n2 = int(input())

printFormat = ""

while n1 <= n2:
    odd = 0
    even = 0
    c = str(n1)
    for k in range(0, len(c)):
        if (k + 1) % 2 == 0:
            even += int(c[k])
        else:
            odd += int(c[k])

    if even == odd:
        printFormat += f"{n1} "
    n1 += 1

print(printFormat)