numbers = input().split(", ")
numbers = list(map(int, numbers))

indicesEvenNums = [k for k in range(0, len(numbers)) if numbers[k] % 2 == 0]

print(indicesEvenNums)