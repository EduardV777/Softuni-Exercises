divisor = int(input())
boundary = int(input())

highest = 0

for k in range (1, boundary + 1):
    if k % divisor == 0:
        if k > highest:
            highest = k

print(highest)