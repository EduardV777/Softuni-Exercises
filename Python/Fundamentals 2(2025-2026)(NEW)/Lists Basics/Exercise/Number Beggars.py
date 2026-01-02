nums = input().split(", ") #separated by , and space
beggars = int(input())

beggarsList = []

for k in range(1, beggars + 1):
    beggarsList.append(0)

del beggars
c = 0

for k in range(0, len(nums)):
    beggarsList[c] += int(nums[k])
    c += 1

    if c >= len(beggarsList):
        c = 0

print(beggarsList)