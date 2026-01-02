n = int(input())

# Special number is when the sum of its digits is 5, 7, or 11

for k in range(1, n + 1):
    sum = 0
    num = str(k)

    for j in range(0, len(num)):
        sum += int(num[j])

    print(num + " ->", end = " ")

    if sum == 5 or sum == 7 or sum == 11:
        print("True")
    else:
        print("False")