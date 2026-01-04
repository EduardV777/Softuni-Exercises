def perfectNum(n = int(input())):

    divisors = []

    for k in range(1, n):
        if n % k == 0:
            divisors.append(k)

    divisorsSum = sum(divisors)

    if divisorsSum == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfectNum()