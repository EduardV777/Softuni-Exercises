n = int(input()) * 2

left = []
right = []

for k in range(0, n // 2):
    number = int(input())
    left.append(number)
    if k == n // 2 - 1:
        for i in range(0, n // 2):
            number = int(input())
            right.append(number)

if sum(right) == sum(left):
    print(f"Yes, sum = {sum(left)}")

else:
    print(f"No, diff = {abs(sum(right) - sum(left))}")