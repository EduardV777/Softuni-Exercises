sumPrime = 0
sumNonPrime = 0

while True:
    n = input()

    if n != "stop":
        prime = True
        n = int(n)

        if n < 0:
            print("Number is negative.")
            continue

        for k in range(2, n):
            if n % k == 0:
                prime = False
                break

        if not prime:
            sumNonPrime += n
        else:
            sumPrime += n

    else:
        break

print(f"Sum of all prime numbers is: {sumPrime}")
print(f"Sum of all non prime numbers is: {sumNonPrime}")