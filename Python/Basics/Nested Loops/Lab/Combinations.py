# x1 + x2 + x3 = n

solutions = 0
x1 = 0
x2 = 0
x3 = 0

n = int(input())

while x1 <= n:
    while x2 <= n:
        while x3 <= n:
            if x1 + x2 + x3 == n:
                solutions += 1

            x3 += 1
        x3 = 0
        x2 += 1
    x2 = 0
    x1 += 1

print(solutions)