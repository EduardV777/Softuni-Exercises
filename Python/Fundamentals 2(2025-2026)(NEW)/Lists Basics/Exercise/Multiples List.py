factor = int(input())
count = int(input())

nums = []

for k in range(1, count + 1):
    nums.append(factor * k)

print(nums)