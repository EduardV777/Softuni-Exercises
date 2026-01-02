n = float(input())

if abs(n) < 1 and not n == 0:
    print("small", end = " ")
elif abs(n) > 1000000:
    print("large", end = " ")

if n == 0:
    print("zero")
elif n < 0:
    print("negative", end = "")
elif n > 0:
    print("positive", end = "")