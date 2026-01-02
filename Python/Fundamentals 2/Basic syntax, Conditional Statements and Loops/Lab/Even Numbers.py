n = int(input())

while n:
    number = int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        break

    n -= 1

if n == 0:
    print("All numbers are even.")