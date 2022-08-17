def sum():
    num = 0

    while num <= 5:
        yield num
        num += 1

    return num

sumVar = sum()
print(sumVar)

print(next(sumVar))
print(next(sumVar))

while True:
    try:
        print(next(sumVar))
    except StopIteration:
        break