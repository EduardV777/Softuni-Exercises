n = int(input())
sHalf = ""

for k in range(1, n + 1):
    print("*" * k)

    if n - k != 0:
        sHalf += ("*" * (n - k)) + "\n"

print(sHalf)