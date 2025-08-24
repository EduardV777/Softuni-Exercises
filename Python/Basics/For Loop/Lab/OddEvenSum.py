n = int(input())
even = 0
odd = 0

for k in range(1, n + 1):
    number = int(input())

    if k % 2 == 0:
        even += number
    else:
        odd += number

if even == odd:
    print(f"Yes\nSum = {even}")
else:
    print(f"No\nDiff = {abs(even - odd)}")