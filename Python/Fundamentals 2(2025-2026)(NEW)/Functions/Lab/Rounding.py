nums = input().split(" ")

def roundValues(numbers):

    numbers = [round(float(k)) for k in numbers]

    return numbers

nums = roundValues(nums)

print(nums)