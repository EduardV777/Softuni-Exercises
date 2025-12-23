n = int(input())
sum = 0

while True:
    number = int(input())
    sum += number

    if sum >= n:
        break

print(sum)