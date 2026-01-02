nums = input().split(" ")
n = int(input())

# for k in range(0, len(nums)):
#     nums[k] = int(nums[k])

while n:
    minimum = 0

    for k in range(0, len(nums)):
        if k == 0:
            minimum = int(nums[k])
            continue
        else:
            if int(nums[k]) < minimum:
                minimum = int(nums[k])

    nums.remove(str(minimum))

    n -= 1


print(", ".join(nums))