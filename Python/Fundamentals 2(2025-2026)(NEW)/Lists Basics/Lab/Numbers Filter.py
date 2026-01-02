n = int(input())
numbers = []
filtered = []
while n:
    num = int(input())
    numbers.append(num)

    n -= 1


comm = input() #even odd negative positive

if comm == "even":
    for k in numbers:
        if k % 2 == 0:
            filtered.append(k)


elif comm == "odd":
    for k in numbers:
        if k % 2 != 0:
            filtered.append(k)

elif comm == "negative":
    for k in numbers:
        if k < 0:
            filtered.append(k)

elif comm == "positive":
    for k in numbers:
        if k >= 0:
            filtered.append(k)

print(filtered)